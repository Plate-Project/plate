# -*- coding:utf-8 -*-
'''
Created on 2014. 8. 19.
@author: seonghyunan
'''

import os
import sys
import json
import traceback
import optparse
import pprint


reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('./common')
sys.path.append('./watchdocs')

from collections import OrderedDict
from flask import Flask 
from flask import redirect
from flask import url_for
from flask import session
from flask import request
from flask import make_response
from flask import jsonify
from flask import render_template

from bs4 import BeautifulSoup

from common.jsonobject import JsonObject
from convmd2html import * 
from common.syntax_highlighting import *
from common.alogger import ALogger


from watchdocs.watch_api_doc import *
from watchdocs.document_trace_queue import *


import server   

app = Flask(__name__, static_url_path = "", static_folder = "static")


#HTTP_METHOD
GET     = 'GET'
POST    = 'POST'
PUT     = 'PUT'
DELETE  = 'DELETE'
HEAD    = 'HEAD'
 

g_config    = None
g_doc_index = None
g_docs      = None
s_dtq       = None


TITLE_TAGS = ['h1', 'h2', 'h3', 'h4']

@app.route('/')
def index(): 
    global g_config
    global g_docs
    global s_dtq


    if not s_dtq.empty():
        event, is_index_file= s_dtq.dequeue() 
        
        if is_index_file:
            total_reload_docs()
        else:
            partial_reload_docs(os.path.split(event.src_path)[1])

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
        API_TITLE=g_config.TITLE,
        IS_SEARCH=g_config.SEARCH_ON,  
        LOGO_TITLE=logo_title,
        LOGO_IMG=logo_img,
        SUPPORT_LANGUAGES=g_config.SUPPORT_LANG,
        DOCS = g_docs.values()
        )

@app.route('/admin')
def admin():
    pp = pprint.PrettyPrinter(indent=4, depth=4)
    config = pp.pformat(g_config.__dict__).replace("u'", "'")
    return render_template("admin.html",
                           config_json= config,
                           indexes=g_doc_index["ORDER"])


@app.route('/documents/<file_name>')
def documents(file_name):
    global g_config

    doc_file = os.path.join(g_config.API_DOC_PATH, file_name)
    body = None
    with open(doc_file, 'r') as f:
        body = f.read().replace('\n', '<br/>')

    return jsonify({'file_name':file_name, 'text':body})



def read_conf(config_path=None): 
    with open(config_path, 'r') as f:
        return json.loads(f.read(), object_hook=JsonObject)

def read_conf_with_order(config_path=None):
    return json.load(open(config_path), object_pairs_hook=OrderedDict)


def reordering(html):
    soup = BeautifulSoup(html)

    up_tags = list()
    for up_tag in soup.h1.next_siblings:
        if up_tag.name in ['pre','blockquote']:
            up_tags.append(up_tag)

    up_tags = reversed(up_tags)
    
    for up_tag in up_tags:
        for prev in up_tag.previous_siblings:
            if prev.name == 'h2':
                prev.insert_after(up_tag)
                break

    return soup


def craete_api_docs():
    global g_doc_index
    global g_config 
    docs = OrderedDict()
    for doc_file in g_doc_index["ORDER"]:
        doc_file = os.path.join(g_config.API_DOC_PATH, doc_file)
        with open(doc_file, 'r') as f:
            html = conv_md2html(f.read())
            docs[os.path.split(doc_file)[1]] = (modifyHtml(highlightSyntax(reordering(html))))


    return docs


def modifyHtml(soup): 
    tags = list()
    [tags.extend(soup.find_all(title_tag)) for title_tag in TITLE_TAGS]
        

    #h1, h2 add id attribute
    for tag in tags:
        id_str = tag.string.lower()
        splitted = id_str.split(' ')

        if len(splitted) >0:
            tag['id'] = '-'.join(splitted)

    return soup.prettify(formatter=None)


def highlightSyntax(soup):  
    code_tags = soup.find_all('code')

    for code in code_tags:  
        if code.has_attr('class'):
            lang = code['class']
            code.parent['class'] = "highlight "+ lang[0]
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
    g_doc_index = read_conf_with_order(os.path.join(g_config.API_DOC_PATH, \
                                    g_config.API_DOC_INDEX_PATH))

    g_docs = None
    g_docs = craete_api_docs()



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
                g_docs[file_name] = (modifyHtml(highlightSyntax(reordering(html))))



def watch_doc_start():
    global s_dtq
    s_dtq = DocumentTraceQueue()
    start_watch(g_config.API_DOC_PATH, g_config.API_DOC_INDEX_PATH, g_doc_index["ORDER"])


def start_test_server():
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        stop_watch()


def start_service_server():
    try:
        server.start(app, port=8080)
    except KeyboardInterrupt:
        stop_watch()
        server.stop()

if __name__ == '__main__':
    p = optparse.OptionParser('-m [test] or [run]')
    p.add_option('-m', dest='mode', type='string')
    options, args = p.parse_args()

    #read config.json
    ALogger.INFO("read config.json")
    g_config = read_conf('config.json')
    
    #create documents  
    total_reload_docs()
    
    #start watch docs 
    watch_doc_start()
   
    
    if options.mode == 'test':
        start_test_server()
    else:
        start_service_server()
    
    
    
