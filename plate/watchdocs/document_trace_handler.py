# -*- coding:utf-8 -*-

from watchdog.events import FileSystemEventHandler
from plate.watchdocs.document_trace_queue import DocumentTraceQueue
from os.path import split


class DocumentTraceHandler(FileSystemEventHandler):
    """
    ``DocumentTraceHandler`` is event handler for API Document files.
    """

    tracing_files = None

    def __init__(self, tracing_files=None):
        """
        Construct method of ``DocumentTraceHandler``.

        :param tracing_files: Files to track
        :return: DocumentTraceHandler instance
        """

        if tracing_files:
            self.tracing_files = tracing_files
        else:
            self.tracing_files = list()

    def on_modified(self, event):
        """
        Event handler about modified.
        If raise modify on api document file or index file such as ``index.json``, enqueue event to DocumentTraceQueue.

        :param event: the event about event handler
        """
        document_trace_queue = DocumentTraceQueue()
        modified_document_trace_file = self.get_document_trace_file(file_name=split(event.src_path)[1])

        if modified_document_trace_file:
            document_trace_queue.enqueue(event=event,
                                         is_index_file=modified_document_trace_file.is_index_file)

    def get_document_trace_file(self, file_name):
        tf_file = None
        for tf in self.tracing_files:
            tf_file_name = split(tf.file_path)[1]
            if tf_file_name == file_name:
                tf_file = tf
                break
        return tf_file
