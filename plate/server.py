# -*- coding:utf-8 -*-

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer

from plate.common.logger import logger


def start(app, port=8080):
    logger.info('Server Start..' + str(port))
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port)
    IOLoop.instance().start()


def stop():
    logger.info('Server Stop..')
    IOLoop.instance().stop()
