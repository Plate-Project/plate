# -*- coding:utf-8 -*-
'''
Created on 2015. 08. 03
@author: AhnSeongHyun
'''

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.path.append('../common')
except NameError:
    pass


class DocumentTraceQueue(object):
    from common import Singleton
    __metaclass__ = Singleton
    trace_queue = []

    def empty(self):
        if len(self.trace_queue) > 0:
            return False
        else:
            return True

    def count(self):
        return len(self.trace_queue)

    def enqueue(self, event, is_index_file):
        self.trace_queue.append((event, is_index_file)) 

    def dequeue(self):
        if self.empty():
            return None
        else:
            import copy
            event = copy.deepcopy(self.trace_queue[0])
            self.trace_queue.remove(event)
            return

    def clear(self):
        self.trace_queue = []