# -*- coding:utf-8 -*-
import unittest
import time

from plate.watchdocs.api_document_observer import APIDocumentObserver
from plate.watchdocs.document_trace_queue import DocumentTraceQueue


class APIDocumentObserverTestCase(unittest.TestCase):

    def setUp(self):

        self.tracing_files = []

        for i in range(0, 10):
            file_path = "./tests/" + str(i) + "_test.txt"
            with open(file_path, "w") as f:
                f.write(str(i))
            self.tracing_files.append(file_path)

    def test_start_stop_watch(self):
        APIDocumentObserver.clear_instance()
        api_doc_observer = APIDocumentObserver(doc_path="./tests/",
                                               doc_index_path=None,
                                               doc_file_path_list=self.tracing_files)

        api_doc_observer.start_watch()
        self.assertEqual(api_doc_observer.is_started, True)
        api_doc_observer.stop_watch()
        self.assertEqual(api_doc_observer.is_started, False)

    def test_on_modified(self):
        APIDocumentObserver.clear_instance()
        api_doc_observer = APIDocumentObserver(doc_path="./tests/",
                                               doc_index_path=None,
                                               doc_file_path_list=self.tracing_files)
        api_doc_observer.start_watch()
        time.sleep(3)

        with open("./tests/0_test.txt", "a+") as f:
            f.write("test")

        time.sleep(3)

        api_doc_observer.stop_watch()
        doc_queue = DocumentTraceQueue()
        self.assertEqual(doc_queue.count(), 1)

    def test_doc_path_exception(self):

        APIDocumentObserver.clear_instance()
        with self.assertRaises(Exception):
            APIDocumentObserver(doc_path=None, doc_index_path=None, doc_file_path_list=self.tracing_files)

    def tearDown(self):

        from os import remove
        from os.path import exists
        for file_path in self.tracing_files:
            if exists(file_path):
                remove(file_path)
