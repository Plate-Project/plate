# -*- coding:utf-8 -*-


def is_absolute(url):
    try:
        from urllib.parse import urlparse, urlencode
    except ImportError:
        from urlparse import urlparse

    if url:
        parsed_url = urlparse(url)
        if bool(parsed_url.netloc):
            return True
        else:
            from os.path import isabs
            return isabs(parsed_url.path)
    else:
        return False


import logging
from logging import Formatter
logging_handler = logging.StreamHandler()
logging_handler.setFormatter(Formatter("[%(asctime)s] : %(message)s [in %(filename)s:%(lineno)d]"))
logger = logging.getLogger('plate')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging_handler)

pst_logging_handler = logging.StreamHandler()
pst_logging_handler.setFormatter(Formatter(""))
pst_logger = logging.getLogger('plate_static_tool')
pst_logger.setLevel(logging.INFO)
pst_logger.addHandler(pst_logging_handler)
