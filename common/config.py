# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''


class Config(object):
    # reading config file
    def __init__(self, result):
        vars(self).update(result)

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def load_conf(conf_file_path):
        import json
        conf = None
        with open(conf_file_path, 'r') as f:
            conf = json.loads(f.read(), object_hook=Config)

        return conf
