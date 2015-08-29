# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

 
class Config(object):

    def __init__(self, result):
        vars(self).update(result)

    def __repr__(self):
        return str(self.__dict__)