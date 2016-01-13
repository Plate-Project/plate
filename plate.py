# -*- coding:utf-8 -*-

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass


from plate.common import logger

from plate import create_app
from plate import start_test_server
from plate import start_service_server


def parse_argument():
    import optparse
    p = optparse.OptionParser('-m [test] or [run] or [convert]')
    try:
        p.add_option('-m', dest='mode', type='string', default='run')
        options, args = p.parse_args()
        return options.mode
    except:
        print(p.get_usage())
        sys.exit()


def test_mode(config):
    app = create_app(config=config)
    from plate.watchdocs import APIDocumentObserver
    api_doc_observer = APIDocumentObserver(doc_path=app.config['API_DOC_PATH'],
                                           doc_index_path=app.config['API_DOC_INDEX_PATH'],
                                           filter_docs=api_doc.toc['ORDER'])
    api_doc_observer.start_watch()
    start_test_server(app=app, port=app.config['PORT'])


def service_mode(config):
    app = create_app(config=config)
    from plate.watchdocs import APIDocumentObserver
    api_doc_observer = APIDocumentObserver(doc_path=app.config['API_DOC_PATH'],
                                           doc_index_path=app.config['API_DOC_INDEX_PATH'],
                                           filter_docs=api_doc.toc['ORDER'])
    api_doc_observer.start_watch()
    start_service_server(app=app, port=app.config['PORT'])


def convert_code(config):
    from os.path import join
    from os.path import isdir
    import os
    import shutil

    try:
        from plate.common import convert_static_html
        rendered_template = convert_static_html(config=config, contents=api_doc.contents)

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

if __name__ == '__main__':
    m = parse_argument()

    from plate.common.config import Config
    config = Config.load_conf('./config.json')

    # create documents
    from plate.api_document import APIDocument
    api_doc = APIDocument(config)

    if m == 'test':
        test_mode(config=config)
    elif m == 'run':
        service_mode(config=config)
    elif m == 'convert':
        convert_code(config=config)
    else:
        raise Exception("Not valid mode")
