# -*- coding:utf-8 -*-

from flask import Flask


def create_app(config=None):
    from plate.views import views_blueprint
    app = Flask(__name__, static_url_path="", static_folder="static")
    configure_app(app, config)

    blueprints = [views_blueprint]
    configure_blueprints(app, blueprints)
    return app


def configure_app(app, config=None):
    if config:
        app.config.from_object(config)


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def start_test_server(app, port=5000):
    try:
        app.run(debug=True, host='0.0.0.0', port=port)
    except KeyboardInterrupt:
        from plate.watchdocs import APIDocumentObserver
        APIDocumentObserver().stop_watch()


def start_service_server(app, port=8080):
    from .server import start
    from .server import stop
    try:
        start(app, port=port)
    except KeyboardInterrupt:
        from plate.watchdocs import APIDocumentObserver
        stop()
        APIDocumentObserver().stop_watch()
