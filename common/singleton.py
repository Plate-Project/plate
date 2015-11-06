# -*- coding:utf-8 -*-

class Singleton(type):
    """
    Singleton Base Class

    Example: ::

        class DocumentTraceQueue(object):
            from common import Singleton
            __metaclass__ = Singleton

    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
