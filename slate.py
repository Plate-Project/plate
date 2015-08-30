# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

import sys
import optparse

try:
    reload(sys)

    sys.setdefaultencoding('utf-8')
    sys.path.append('./common')
    sys.path.append('./watchdocs')
except NameError:
    pass


from flask import Flask
from flask import render_template
from api_document import  APIDocument
import watchdocs
import server

app = Flask(__name__, static_url_path="", static_folder="static")
api_doc = None

from common.config import Config
app.config.from_object(Config.load_conf('config.json'))


#todo : 이름 변경 하기
s_dtq = None # watch_doc_queue




@app.route('/')
def index():
    # global s_dtq
    #
    # if not s_dtq.empty():
    #     api_doc.total_reload_docs()
    #     s_dtq.clear()

    temp = [str(lang) for lang in app.config['SUPPORT_LANG']]
    app.config['SUPPORT_LANG'] = temp

    logo_title = None
    logo_img = None

    if 'LOGO_IMG' in app.config:
        logo_img = app.config['LOGO_IMG']

    if 'LOGO_TITLE' in app.config:
        logo_title = app.config['LOGO_TITLE']

    return render_template("index.html",
                           API_TITLE=app.config['TITLE'],
                           IS_SEARCH=app.config['SEARCH_ON'],
                           LOGO_TITLE=logo_title,
                           LOGO_IMG=logo_img,
                           SUPPORT_LANGUAGES=app.config['SUPPORT_LANG'],
                           DOCS=api_doc.contents,
                           COPYRIGHT=app.config['COPYRIGHT']
                           )







# def partial_reload_docs(file_name):
#     ALogger.INFO("partial_reload_docs")
#
#     global g_docs
#     global g_doc_index
#
#     for doc_file in g_doc_index["ORDER"]:
#         if file_name == os.path.split(doc_file)[1]:
#
#             from os.path import join
#             doc_file = join(app.config['API_DOC_PATH'], doc_file)
#             with open(doc_file, 'r') as f:
#                 html = conv_md2html(f.read())
#                 g_docs[file_name] = modify_html(highlight_syntax(reordering(html)))


def watch_doc_start():
    pass
    # global s_dtq
    # s_dtq = watchdocs.DocumentTraceQueue()
    # watchdocs.start_watch(app.config['API_DOC_PATH'], app.config['API_DOC_INDEX_PATH'], g_doc_index["ORDER"])


if __name__ == '__main__':
    p = optparse.OptionParser('-m [test] or [run]')
    p.add_option('-m', dest='mode', type='string')
    options, args = p.parse_args()

    # create documents
    api_doc = APIDocument(app.config['API_DOC_PATH'], app.config['API_DOC_INDEX_PATH'])

    # start watch docs
    watch_doc_start()


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

    if options.mode == 'test':
        start_test_server(app.config['PORT'])
    else:
        start_service_server(app.config['PORT'])
