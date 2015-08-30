# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

import sys
import copy

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.path.append('../common')
except NameError:
    pass


class DocumentTraceQueue(object):
    from common import Singleton
    __metaclass__ = Singleton
    eventQueue = list()

    def empty(self):
        if len(self.eventQueue) > 0:
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
            self.eventQueue.remove(event)
            return

    def clear(self):
        self.eventQueue = []