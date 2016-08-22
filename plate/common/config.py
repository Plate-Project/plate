# -*- coding:utf-8 -*-

import json


class Config(object):
    """
    Read JSON Format config file.
    """

    def __init__(self, result):
        vars(self).update(result)

    def __repr__(self):
        return str(self.__dict__)

    def exist(self, var):
        if var in self.__dict__:
            return True
        else:
            return False

    @staticmethod
    def load_conf(conf_file_path):
        """
        Read ``.json`` file

        :param conf_file_path: ``.json`` file path
        :return: conf instance
        """
        with open(conf_file_path, 'r') as f:
            conf = json.loads(f.read(), object_hook=Config)
        return conf
