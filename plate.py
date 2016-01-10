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
from api_document import APIDocument


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

def start_test_server(port=5000):
    try:
        app.run(debug=True, host='0.0.0.0', port=port)
    except KeyboardInterrupt:
        from watchdocs import stop_watch
        stop_watch()

def start_service_server(port=8080):
    import server
    try:
        server.start(app, port=port)
    except KeyboardInterrupt:
        from watchdocs import stop_watch
        stop_watch()
        server.stop()

if __name__ == '__main__':
    m = parse_argument()

    from common.config import Config
    config = Config.load_conf('config.json')

    # create documents
    api_doc = APIDocument(config)

    if m == 'test':
        from watchdocs import start_watch
        app = create_app(config=config, blueprints=[views_blueprint])
        # start watch docs
        start_watch(app.config['API_DOC_PATH'],
                    app.config['API_DOC_INDEX_PATH'],
                    api_doc.toc['ORDER'])
        start_test_server(app.config['PORT'])
    elif m == 'run':
        from watchdocs import start_watch
        app = create_app(config=config, blueprints=[views_blueprint])
        # start watch docs
        start_watch(app.config['API_DOC_PATH'],
                    app.config['API_DOC_INDEX_PATH'],
                    api_doc.toc['ORDER'])
        start_service_server(app.config['PORT'])

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
