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


import logging
from logging import Formatter
logging_handler = logging.StreamHandler()
logging_handler.setFormatter(Formatter("[%(asctime)s] : %(message)s [in %(filename)s:%(lineno)d]"))
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_handler)

from flask import Flask
from flask import render_template
from api_document import APIDocument
import watchdocs
import server


app = Flask(__name__, static_url_path="", static_folder="static")

_g_api_doc = None


@app.route('/')
def index():

    document_trace_queue = watchdocs.DocumentTraceQueue()
    if not document_trace_queue.empty():
        _g_api_doc.total_reload_docs()
        document_trace_queue.clear()

    temp = [str(lang) for lang in app.config['SUPPORT_LANG']]
    app.config['SUPPORT_LANG'] = temp

    logo_title = None
    logo_img = None

    if 'LOGO_IMG' in app.config:
        logo_img = app.config['LOGO_IMG']

    if 'LOGO_TITLE' in app.config:
        logo_title = app.config['LOGO_TITLE']

    from datetime import datetime
    return render_template("index.html",
                           API_TITLE=app.config['TITLE'],
                           IS_SEARCH=app.config['SEARCH_ON'],
                           LOGO_TITLE=logo_title,
                           LOGO_IMG=logo_img,
                           SUPPORT_LANGUAGES=app.config['SUPPORT_LANG'],
                           DOCS=_g_api_doc.contents,
                           COPYRIGHT=app.config['COPYRIGHT'],
                           FAVICON=app.config['FAVICON'],
                           timestamp=datetime.now().strftime("%Y%m%d%H%M%S")
                           )


if __name__ == '__main__':
    import optparse
    p = optparse.OptionParser('-m [test] or [run] or [convert]')
    p.add_option('-m', dest='mode', type='string', default='run')
    options, args = p.parse_args()

    from common.config import Config
    config = Config.load_conf('config.json')

    # create documents
    _g_api_doc = APIDocument(config.API_DOC_PATH,
                             config.API_DOC_INDEX_PATH)

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
        app.config.from_object(config)
        # start watch docs
        watchdocs.start_watch(app.config['API_DOC_PATH'],
                              app.config['API_DOC_INDEX_PATH'],
                              _g_api_doc.toc['ORDER'])
        start_test_server(app.config['PORT'])
    elif options.mode == 'run':
        app.config.from_object(config)
        # start watch docs
        watchdocs.start_watch(app.config['API_DOC_PATH'],
                              app.config['API_DOC_INDEX_PATH'],
                              _g_api_doc.toc['ORDER'])
        start_service_server(app.config['PORT'])

    elif options.mode == 'convert':
        from os.path import join
        from os.path import isdir
        import os
        import shutil

        try:
            from common import convert_static_html
            rendered_template = convert_static_html(config=config, contents=_g_api_doc.contents)

            path = "./static"
            dirs = os.listdir(path)

            if not isdir(config.STATIC.DIR):
                os.mkdir(config.STATIC.DIR)

            for d in dirs:
                src_dir = join(path, d)
                dst_dir = join(config.STATIC.DIR, d)
                if isdir(dst_dir):
                    shutil.rmtree(dst_dir)
                shutil.copytree(src_dir, dst_dir)

            with open(join(config.STATIC.DIR, config.STATIC.HTML), 'w') as f:
                f.write(rendered_template)

        except Exception as e:
            logger.exception(e) 
            if isdir(config.STATIC.DIR):
                shutil.rmtree(config.STATIC.DIR)

            import traceback
            logger.error(traceback.format_exc())
