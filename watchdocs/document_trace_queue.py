# -*- coding:utf-8 -*-
__author__ = 'ash84'

import sys
import copy 
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append('../common') 

from watchdog.observers import Observer
from watchdog.observers.api import EventQueue 

from common.singleton import Singleton
from common.alogger import ALogger

class DocumentTraceQueue(object):
    __metaclass__ = Singleton
    eventQueue = list()

    def empty(self):
        if len(self.eventQueue) >0:
            return False
        else:
            return True

    def enqueue(self, event, is_index_file):
        self.eventQueue.append((event, is_index_file)) 

    def dequeue(self):
        if self.empty():
            return None
        else:
            event = copy.deepcopy(self.eventQueue[0])
            self.eventQueue.remove(self.eventQueue[0])
            return

    def clear(self):
         self.eventQueue = []