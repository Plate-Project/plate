# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

import os
import sys

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except NameError:
    pass

from watchdog.events import FileSystemEventHandler


class DocumentTraceHandler(FileSystemEventHandler):

    filter_files = None

    def __init__(self, doc_index_path, filter_docs):
        self.filter_files = list()

        for doc in filter_docs:
            self.filter_files.append(os.path.split(doc)[1])
        self.filter_files.append(os.path.split(doc_index_path)[1])

    def on_modified(self, event):
        from .document_trace_queue import DocumentTraceQueue
        document_trace_queue = DocumentTraceQueue()

        modified_file = os.path.split(event.src_path)[1]

        if self.is_filtering(modified_file): 
                document_trace_queue.enqueue(event, self.is_index_file(modified_file))

    def is_index_file(self, file_name):
        last = len(self.filter_files)-1
        if file_name in self.filter_files[last]:
            return True
        else:
            return False

    def is_filtering(self, file_name): 
        if file_name in self.filter_files:
            return True
        else:
            return False
