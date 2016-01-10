# -*- coding:utf-8 -*-

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass

from common import logger
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop 


def start(app, port=8080):
    logger.info('Server Start..' + str(port))
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port)
    IOLoop.instance().start()


def stop():
    logger.info('Server Stop..')
    IOLoop.instance().stop()