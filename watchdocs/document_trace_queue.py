# -*- coding:utf-8 -*-
try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.path.append('../common')
except NameError:
    pass


class DocumentTraceQueue(object):
    """
    Queue of modification, inserted, deleted document.
    """
    from common import Singleton
    __metaclass__ = Singleton
    trace_queue = []

    def is_empty(self):
        """
        Is empty trace_queue?
        :return: True or False
        """

        if len(self.trace_queue) > 0:
            return False
        else:
            return True

    def count(self):
        """
        Count of trace_queue
        :return: count
        """
        return len(self.trace_queue)

    def enqueue(self, event, is_index_file):
        """
        Enqueue event to trace_queue

        :param event: insert/update/del event
        :param is_index_file: True or False
        """
        self.trace_queue.append((event, is_index_file))

    def dequeue(self):
        """
        Dequeue event
        Return the copy of top event in trace_queue

        :return: event
        """
        if self.empty():
            return None
        else:
            import copy
            event = copy.deepcopy(self.trace_queue[0])
            self.trace_queue.remove(event)
            return

    def clear(self):
        """
        Remove all trace_queue
        :return:
        """
        self.trace_queue = []
