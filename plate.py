# -*- coding:utf-8 -*-

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass

import optparse

from plate import create_app
from plate import start_service_server
from plate import start_test_server
from plate.api_document import APIDocument
from plate.common.config import Config
from plate.watchdocs.api_document_observer import APIDocumentObserver


def parse_argument():
    p = optparse.OptionParser('-m [test] or [run]')
    try:
        p.add_option('-m', dest='mode', type='string', default='run')
        options, args = p.parse_args()
        return options.mode
    except:
        print(p.get_usage())
        sys.exit()


def test_mode(app):
    start_test_server(app=app, port=app.config['PORT'])


def service_mode(app):
    start_service_server(app=app, port=app.config['PORT'])


if __name__ == '__main__':
    m = parse_argument()

    config = Config.load_conf('./config.json')

    # create documents
    api_doc = APIDocument(config)

    app = create_app(config=config)
    api_doc_observer = APIDocumentObserver(doc_path=app.config['API_DOC_PATH'],
                                           doc_index_path=app.config['API_DOC_INDEX_PATH'],
                                           doc_file_path_list=api_doc.toc['ORDER'])
    api_doc_observer.start_watch()
    if m == 'test':
        test_mode(app=app)
    elif m == 'run':
        service_mode(app=app)
    else:
        raise Exception("Not valid mode")
