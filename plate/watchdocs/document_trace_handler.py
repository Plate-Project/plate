# -*- coding:utf-8 -*-

from watchdog.events import FileSystemEventHandler


class DocumentTraceHandler(FileSystemEventHandler):
    """
    ``DocumentTraceHandler`` is event handler for API Document files.
    """

    filter_files = None

    def __init__(self, doc_index_path, filter_docs):
        """
        Construct method of ``DocumentTraceHandler``.

        :param doc_index_path: API Document Index Path.(``index.json``)
        :param filter_docs: Document file list ``ORDER`` in ``index.json``
        :return: DocumentTraceHandler instance
        """
        self.filter_files = list()
        from os.path import split
        for doc in filter_docs:
            self.filter_files.append(split(doc)[1])
        self.filter_files.append(split(doc_index_path)[1])

    def on_modified(self, event):
        """
        Event handler about modified.
        If raise modify on api document file or index file such as ``index.json``, enqueue event to DocumentTraceQueue.

        :param event: the event about event handler
        """
        from .document_trace_queue import DocumentTraceQueue
        from os.path import split
        document_trace_queue = DocumentTraceQueue()
        modified_file = split(event.src_path)[1]
        document_trace_queue.enqueue(event, self.is_index_file(modified_file))

    def is_index_file(self, file_name):
        """
        Check index file.
        If index file, return ``True``, Else return ``False``.

        :param file_name: file name
        :return: True or False
        """
        last = len(self.filter_files)-1
        if file_name in self.filter_files[last]:
            return True
        else:
            return False

