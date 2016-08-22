# -*- coding:utf-8 -*-
import requests
from flask_testing import LiveServerTestCase


class ViewTestCase(LiveServerTestCase):
    def create_app(self):
        from plate.app import create_app
        from plate.api_document import APIDocument
        from plate.common.config import Config
        config = Config.load_conf('./config.json')
        api_doc = APIDocument(config)
        app = create_app(config=config)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def test_server_is_up_and_running(self):
        response = requests.get(self.get_server_url())
        self.assertEqual(response.status_code, 200)