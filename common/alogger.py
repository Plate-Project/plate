# -*- coding:utf-8 -*-
'''
Created on 2014. 8. 19.
@author: seonghyunan
'''


import logging 
import sys
from time import strftime

import inspect
import os 

LOG_DIR_PATH = './log/'
LOG_FILE_FORMAT = 'slate_%Y_%m_%d.log'

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s][%(levelname)s] - %(message)s')

class ALogger(object):
    
    @staticmethod
    def INFO(var=None):
        prefix = os.path.split(sys._getframe(1).f_code.co_filename)[1] +'::'+sys._getframe(1).f_code.co_name + "()"
        logging.info(prefix + '\t'+str(var))

    @staticmethod
    def DEBUG(var=None): 
        prefix = os.path.splitdrive(sys._getframe(1).f_code.co_filename)[1] +'::'+sys._getframe(1).f_code.co_name + "()"
        logging.debug(prefix + '\t'+str(var))


    @staticmethod
    def WARNING(var=None): 
        prefix = os.path.splitdrive(sys._getframe(1).f_code.co_filename)[1] +'::'+sys._getframe(1).f_code.co_name + "()"
        logging.warning(prefix + '\t'+str(var))


    @staticmethod
    def ERROR(var=None): 
        prefix = os.path.splitdrive(sys._getframe(1).f_code.co_filename)[1] +'::'+sys._getframe(1).f_code.co_name + "()"
        logging.error(prefix + '\t'+str(var))


    @staticmethod
    def CRITICAL(var=None): 
        prefix = os.path.splitdrive(sys._getframe(1).f_code.co_filename)[1] +'::'+sys._getframe(1).f_code.co_name + "()"
        logging.critical(prefix + '\t'+str(var))

    @staticmethod
    def EXCEPTION(var=None): 
        prefix = os.path.splitdrive(sys._getframe(1).f_code.co_filename)[1] +'::'+sys._getframe(1).f_code.co_name + "()"
        logging.exception(prefix + '\t'+str(var))

if __name__ == '__main__':
    ALogger.INFO('TEST')