# -*- coding:utf-8 -*-


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
