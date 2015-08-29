# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

import os
import sys
import json
import optparse

try:
    reload(sys)

    sys.setdefaultencoding('utf-8')
    sys.path.append('./common')
    sys.path.append('./watchdocs')
except NameError:
    pass

from collections import OrderedDict
from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup

from common import ALogger
from common import conv_md2html
from common import syntax_highlight
from common import Config

import watchdocs
import server

app = Flask(__name__, static_url_path="", static_folder="static")

g_config = None
g_doc_index = None
g_docs = None
s_dtq = None

TITLE_TAGS = ['h1', 'h2', 'h3', 'h4']


@app.route('/')
def index():
    global g_config
    global g_docs
    global s_dtq

    if not s_dtq.empty():
        total_reload_docs()
        s_dtq.clear()

    temp = list()
    [temp.append(str(lang)) for lang in g_config.SUPPORT_LANG]
    g_config.SUPPORT_LANG = temp

    logo_title = None
    logo_img = None

    if 'LOGO_IMG' in g_config.__dict__:
        logo_img = g_config.LOGO_IMG

    if 'LOGO_TITLE' in g_config.__dict__:
        logo_title = g_config.LOGO_TITLE

    return render_template("index.html",
        API_TITLE = g_config.TITLE,
        IS_SEARCH = g_config.SEARCH_ON,
        LOGO_TITLE = logo_title,
        LOGO_IMG = logo_img,
        SUPPORT_LANGUAGES=g_config.SUPPORT_LANG,
        DOCS = g_docs.values(),
        COPYRIGHT = g_config.COPYRIGHT
        )


def read_conf(config_path=None):
    with open(config_path, 'r') as f:
        return json.loads(f.read(), object_hook=Config)


def read_conf_with_order(config_path=None):
    return json.load(open(config_path), object_pairs_hook=OrderedDict)


def reordering(html):
    soup = BeautifulSoup(html)

    up_tags = list()
    for up_tag in soup.h1.next_siblings:
        if up_tag.name in ['pre', 'blockquote']:
            up_tags.append(up_tag)

    up_tags = reversed(up_tags)

    for up_tag in up_tags:
        for prev in up_tag.previous_siblings:
            if prev.name == 'h2':
                prev.insert_after(up_tag)
                break
    return soup


def create_api_docs():
    global g_doc_index
    global g_config 
    docs = OrderedDict()
    for doc_file in g_doc_index["ORDER"]:
        doc_file = os.path.join(g_config.API_DOC_PATH, doc_file)
        with open(doc_file, 'r') as f:
            html = conv_md2html(f.read())
            docs[os.path.split(doc_file)[1]] = (modify_html(highlight_syntax(reordering(html))))

    return docs


def modify_html(soup):
    tags = list()
    [tags.extend(soup.find_all(title_tag)) for title_tag in TITLE_TAGS]

    # h1, h2 add id attribute
    for tag in tags:
        id_str = tag.string.lower()
        splitted = id_str.split(' ')

        if len(splitted) > 0:
            tag['id'] = '-'.join(splitted)

    return soup.prettify(formatter=None)


def highlight_syntax(soup):
    code_tags = soup.find_all('code')

    for code in code_tags:
        if code.has_attr('class'):
            lang = code['class']
            code.parent['class'] = "highlight " + lang[0]
            del code['class']
            code.name = "span"
            code.parent.replaceWith(syntax_highlight(lang[0], code.string))

    return soup


def total_reload_docs():
    ALogger.INFO("total_reload_docs")
    global g_doc_index
    global g_config
    global g_docs

    g_doc_index = None
    g_doc_index = read_conf_with_order(os.path.join(g_config.API_DOC_PATH, g_config.API_DOC_INDEX_PATH))

    g_docs = None
    g_docs = create_api_docs()


def partial_reload_docs(file_name):
    ALogger.INFO("partial_reload_docs")

    global g_docs
    global g_doc_index
    global g_config

    for doc_file in g_doc_index["ORDER"]:
        if file_name == os.path.split(doc_file)[1]:

            doc_file = os.path.join(g_config.API_DOC_PATH, doc_file)
            with open(doc_file, 'r') as f:
                html = conv_md2html(f.read())
                g_docs[file_name] = modify_html(highlight_syntax(reordering(html)))


def watch_doc_start():
    global s_dtq
    s_dtq = watchdocs.DocumentTraceQueue()
    watchdocs.start_watch(g_config.API_DOC_PATH, g_config.API_DOC_INDEX_PATH, g_doc_index["ORDER"])


def start_test_server(port=5000):
    try:
        app.run(debug=True, host='0.0.0.0', port=port)
    except KeyboardInterrupt:
        watchdocs.stop_watch()


def start_service_server(port=8080):
    try:
        server.start(app, port=port)
    except KeyboardInterrupt:
        watchdocs.stop_watch()
        server.stop()

if __name__ == '__main__':
    p = optparse.OptionParser('-m [test] or [run]')
    p.add_option('-m', dest='mode', type='string')
    options, args = p.parse_args()

    # read config.json
    ALogger.INFO("read config.json")
    g_config = read_conf('config.json')

    # create documents
    total_reload_docs()

    # start watch docs
    watch_doc_start()

    if options.mode == 'test':
        start_test_server(g_config.PORT)
    else:
        start_service_server(g_config.PORT)
