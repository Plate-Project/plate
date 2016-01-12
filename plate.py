# -*- coding:utf-8 -*-

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass


from common import logger
from flask import Flask
from views import views_blueprint


def create_app(config=None, blueprints=None):
    app = Flask(__name__, static_url_path="", static_folder="static")
    configure_app(app, config)
    configure_blueprints(app, blueprints)
    return app


def configure_app(app, config=None):
    if config:
        app.config.from_object(config)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


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


def start_test_server(app, port=5000):
    try:
        app.run(debug=True, host='0.0.0.0', port=port)
    except KeyboardInterrupt:
        from watchdocs import APIDocumentObserver
        APIDocumentObserver().stop_watch()


def start_service_server(app, port=8080):
    import server
    try:
        server.start(app, port=port)
    except KeyboardInterrupt:
        from watchdocs import APIDocumentObserver
        APIDocumentObserver().stop_watch()
        server.stop()


def test_mode(config):
    app = create_app(config=config, blueprints=[views_blueprint])
    from watchdocs import APIDocumentObserver
    api_doc_observer = APIDocumentObserver(doc_path=app.config['API_DOC_PATH'],
                                           doc_index_path=app.config['API_DOC_INDEX_PATH'],
                                           filter_docs=api_doc.toc['ORDER'])
    api_doc_observer.start_watch()
    start_test_server(app=app, port=app.config['PORT'])


def service_mode(config):
    app = create_app(config=config, blueprints=[views_blueprint])
    from watchdocs import APIDocumentObserver
    api_doc_observer = APIDocumentObserver(doc_path=app.config['API_DOC_PATH'],
                                           doc_index_path=app.config['API_DOC_INDEX_PATH'],
                                           filter_docs=api_doc.toc['ORDER'])
    api_doc_observer.start_watch()
    start_service_server(app=app, port=app.config['PORT'])

if __name__ == '__main__':
    m = parse_argument()

    from common.config import Config
    config = Config.load_conf('config.json')

    # create documents
    from api_document import APIDocument
    api_doc = APIDocument(config)

    if m == 'test':
        test_mode(config=config)
    elif m == 'run':
        service_mode(config=config)
    elif m == 'convert':
        from os.path import join
        from os.path import isdir
        import os
        import shutil

        try:
            from common import convert_static_html
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
