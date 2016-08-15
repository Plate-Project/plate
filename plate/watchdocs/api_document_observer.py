# -*- coding:utf-8 -*-

from future.utils import with_metaclass
from watchdog.observers import Observer

from plate.common.singleton_meta import SingletonMeta
from plate.common.logger import logger
from plate.watchdocs.document_trace_file import DocumentTraceFile
from plate.watchdocs.document_trace_handler import DocumentTraceHandler


class APIDocumentObserver(with_metaclass(SingletonMeta, object)):
    """
    ``APIDocumentObserver`` is observer of API Documents.
    """

    def __init__(self, doc_path=None, doc_index_path=None, doc_file_path_list=None):
        """
        Construct method of ``APIDocumentObserver``.

        :param doc_path: API Document Directory path
        :param doc_index_path: API Document index path
        :param doc_file_path_list: Document file list ``ORDER`` in ``index.json``
        :return:  APIDocumentObserver Singleton instance
        """
        if doc_path:
            if doc_file_path_list and isinstance(doc_file_path_list, list):
                tracing_files = [DocumentTraceFile(tracing_file_path=f) for f in doc_file_path_list]
            else:
                tracing_files = list()

            if doc_index_path:
                tracing_files.append(DocumentTraceFile(tracing_file_path=doc_index_path, is_index_file=True))

            event_handler = DocumentTraceHandler(tracing_files=tracing_files)
            self.observer = Observer()
            self.observer.schedule(event_handler, doc_path, recursive=True)
        else:
            raise Exception("doc_path is None.")

    def start_watch(self):
        """
        Start watch docs
        """

        if self.observer:
            self.observer.start()
            logger.info("Start watchdocs..")
        else:
            pass

    @property
    def is_started(self):
        """
        After run ``start_watch()``, ``is_started`` is True, or False.

        :return: True | False
        """

        if self.observer:
            return self.observer.is_alive()
        return False

    def stop_watch(self):
        """
        Stop watch docs
        """

        if self.observer and self.observer.is_alive():
            self.observer.stop()
            self.observer.join()

            logger.info("Stop watchdocs..")
