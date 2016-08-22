# -*- coding:utf-8 -*-

from copy import deepcopy

from future.utils import with_metaclass
from watchdog.events import FileSystemEvent

from plate.common.singleton_meta import SingletonMeta


class DocumentTraceQueue(with_metaclass(SingletonMeta, object)):
    """
    Queue of modification, inserted, deleted document.
    """

    trace_queue = []

    def is_empty(self):
        # type: () -> object
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
        if isinstance(event, FileSystemEvent) and isinstance(is_index_file, bool):
            self.trace_queue.append((event, is_index_file))
        else:
            raise TypeError('event of is_index_file type error.')

    def dequeue(self):
        """
        Dequeue event
        Return the copy of top event in trace_queue

        :return: event
        """
        if self.is_empty():
            return None
        else:
            event = deepcopy(self.trace_queue[0])
            self.trace_queue.remove(event)
            return event

    def clear(self):
        """
        Remove all trace_queue
        """
        self.trace_queue = []
