# -*- coding:utf-8 -*-
import unittest

from watchdog.events import FileModifiedEvent

from plate.watchdocs import DocumentTraceFile


class DocumentTraceFileTestCase(unittest.TestCase):

    def test(self):
        with self.assertRaises(Exception):
            DocumentTraceFile(tracing_file_path=None)
