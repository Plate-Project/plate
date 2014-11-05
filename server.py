# -*- coding:utf-8 -*-
'''
Created on 2014. 8. 19.
@author: seonghyunan
'''

import os
import sys
import json
import traceback
import optparse

reload(sys)
sys.setdefaultencoding('utf-8')

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop 
from common.alogger import ALogger


def start(app, port=8080):
    ALogger.INFO('Server Start..' + str(port))
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port)
    IOLoop.instance().start()
    
def stop():
    ALogger.INFO('Server Stop..')
    IOLoop.instance().stop()