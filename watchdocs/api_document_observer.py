# -*- coding:utf-8 -*-

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.path.append('../common')
except NameError:
    pass

from common import logger
from common import SingletonMeta
from future.utils import with_metaclass


class APIDocumentObserver(with_metaclass(SingletonMeta, object)):

    def __init__(self, doc_path=None, doc_index_path=None, filter_docs=None):
        """
        Construct method of ``APIDocumentObserver``.

        :param doc_path: API Document Directory path
        :param doc_index_path: API Document index path
        :param filter_docs: Document file list ``ORDER`` in ``index.json``
        :return:  APIDocumentObserver Singleton instance
        """
        from watchdog.observers import Observer
        from .document_trace_handler import DocumentTraceHandler

        if doc_path and doc_index_path:
            event_handler = DocumentTraceHandler(doc_index_path, filter_docs)
            self.observer = Observer()
            self.observer.schedule(event_handler, doc_path, recursive=True)

    def start_watch(self):
        """
        Start watch docs
        """

        if self.observer:
            self.stop_watch()
            self.observer.start()
            logger.info("Start watchdocs..")
        else:
            pass

    def stop_watch(self):
        """
        Stop watch docs
        """

        if self.observer:
            self.observer.stop()
            self.observer.join()

            logger.info("Stop watchdocs..")
