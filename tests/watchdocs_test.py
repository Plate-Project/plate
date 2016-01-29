# -*- coding:utf-8 -*-
import unittest

from plate.watchdocs import DocumentTraceQueue
from plate.watchdocs import DocumentTraceHandler
from plate.watchdocs import APIDocumentObserver
from plate.watchdocs import DocumentTraceFile


class DocumentTraceQueueTestCase(unittest.TestCase):

    def setUp(self):
        self.docq = DocumentTraceQueue()

        if self.docq:
            self.docq.clear()
        self.docq.enqueue(event="Test", is_index_file=True)

    def test_is_empty(self):
        self.assertEqual(self.docq.is_empty(), False)
        self.docq.clear()
        self.assertEqual(self.docq.is_empty(), True)

    def count(self):
        self.assertEqual(self.docq.count(), 1)
        self.docq.enqueue(event="Test", is_index_file=False)
        self.assertEqual(self.docq.count(), 2)

    def test_clear(self):
        self.docq.clear()
        self.assertEqual(self.docq.count(), 0)

    def test_enqueue(self):
        self.docq.enqueue(event="Test3", is_index_file=False)
        self.assertEqual(self.docq.count(), 2)

        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", None))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", 1))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", "test"))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", True))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", []))
        self.assertRaises(Exception, self.docq.enqueue, ("TEST1", {}))

    def test_dequeue(self):
        t = self.docq.dequeue()
        self.assertEqual(t[0], "Test")
        self.assertEqual(t[1], True)
        self.assertEqual(self.docq.count(), 0)


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
        import time
        time.sleep(3)

        with open("./tests/0_test.txt", "a+") as f:
            f.write("test")

        time.sleep(3)

        api_doc_observer.stop_watch()
        doc_queue = DocumentTraceQueue()
        self.assertEqual(doc_queue.count(), 1)

    def tearDown(self):

        from os import remove
        from os.path import exists
        for file_path in self.tracing_files:
            if exists(file_path):
                remove(file_path)
