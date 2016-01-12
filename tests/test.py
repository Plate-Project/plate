# -*- coding:utf-8 -*-

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.path.append('./')
except NameError:
    pass

import unittest


class ConverterMDtoHTMLTest(unittest.TestCase):
    """
    Test for converting markdown format file to HTML
    """
    def setUp(self):
        import glob
        path = './document/*.md'
        files = glob.glob(path)

        import codecs
        self.test_file_contents = []
        for file_name in files:
            with codecs.open(file_name, 'r', encoding='utf-8') as f:
                self.test_file_contents.append(f.read())

    def tearDown(self):
        pass

    def test_conv_md_to_html(self):
        try:
            from plate.common import conv_md_to_html

            for fc in self.test_file_contents:
                conv_md_to_html(fc)
                # todo : validate html

        except Exception as e:
            import traceback
            self.fail(traceback.format_exc())


class APIDocumentTest(unittest.TestCase):
    """
    Test for APIDocument Class
    """

    def setUp(self):
        self.testing_codes = []

        from plate.common import Config
        self.config = Config.load_conf('./config.json')

    def tearDown(self):
        pass

    def test_api_doc(self):
        try:
            # create documents
            from plate.api_document import APIDocument
            api_doc = APIDocument(self.config)
            if api_doc.contents:
                pass
                # todo : validate html
            else:
                self.fail("no contents")

        except Exception as e:
            import traceback
            self.fail(traceback.format_exc())


if __name__ == '__main__':
    unittest.main()