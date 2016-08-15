# -*- coding:utf-8 -*-
import unittest

from plate.common.utils import is_absolute


class UtilsTestCase(unittest.TestCase):
    def test_is_absolute(self):
        try:
            self.assertEqual(is_absolute(None), False)
            self.assertEqual(is_absolute("../test/test.php"), False)
            self.assertEqual(is_absolute("/test/test.php"), True)
            self.assertEqual(is_absolute("http://test/test.php"), True)
            self.assertEqual(is_absolute("test.php"), False)
        except Exception as e:
            import traceback
            self.fail(traceback.format_exc())

