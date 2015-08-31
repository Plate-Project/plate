# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

try:
    import sys
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


@app.route('/')
def index():

    document_trace_queue = watchdocs.DocumentTraceQueue()

    if not document_trace_queue.empty():
        api_doc.total_reload_docs()
        document_trace_queue.clear()

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

if __name__ == '__main__':
    import optparse
    p = optparse.OptionParser('-m [test] or [run]')
    p.add_option('-m', dest='mode', type='string')
    options, args = p.parse_args()

    # create documents
    api_doc = APIDocument(app.config['API_DOC_PATH'], app.config['API_DOC_INDEX_PATH'])

    # start watch docs
    watchdocs.start_watch(app.config['API_DOC_PATH'],
                          app.config['API_DOC_INDEX_PATH'],
                          api_doc.toc['ORDER'])


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
