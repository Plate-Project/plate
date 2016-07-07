# -*- coding:utf-8 -*-
import unittest

from plate.app import configure_app
from plate.app import configure_blueprints
from plate.app import start_test_server
from plate.app import start_service_server

import requests

class AppTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_configure_app(self):
        pass


    def test_configure_buleprints(self):
        from flask import Flask, Blueprint
        app = Flask(__name__, static_url_path="", static_folder="static")

        page1 = Blueprint('page1', __name__, template_folder='templates')
        page2 = Blueprint('page2', __name__, template_folder='templates')
        page3 = Blueprint('page3', __name__, template_folder='templates')

        configure_blueprints(app, [page1, page2, page3])
        self.assertEqual(len(app.blueprints), 3)
        self.assertEqual(app.blueprints['page1'], page1)
        self.assertEqual(app.blueprints['page2'], page2)
        self.assertEqual(app.blueprints['page3'], page3)


    def test_start_test_server(self):
        pass


    def test_start_service_server(self):
        pass