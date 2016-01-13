# -*- coding:utf-8 -*-


def is_absolute(url):
    try:
        from urlparse import urlparse
    except ImportError as e:
        from urllib.parse import urlparse
    return bool(urlparse(url).netloc)


import logging
from logging import Formatter
logging_handler = logging.StreamHandler()
logging_handler.setFormatter(Formatter("[%(asctime)s] : %(message)s [in %(filename)s:%(lineno)d]"))
logger = logging.getLogger('plate')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_handler)

