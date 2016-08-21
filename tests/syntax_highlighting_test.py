# -*- coding:utf-8 -*-
import unittest

from plate.common.syntax_highlighting import syntax_highlight


class SyntaxHighlightingTestCase(unittest.TestCase):

    def test_syntax_highlight(self):
        code = """
        def a():
            print "a"
        """
        example_python_code = syntax_highlight(lang="python", code=code)

        # code highlighting test
        self.assertEqual(self._in_code_highlight(lang="python", result=example_python_code), True)

        # exception test
        with self.assertRaises(Exception):
            syntax_highlight(lang=None, code=None)

    def _in_code_highlight(self, lang, result):
            if ("highlight " + lang) in result:
                return True
            return False