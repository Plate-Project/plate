# -*- coding:utf-8 -*-


class SingletonMeta(type):
    """
    Singleton Base Class

    Example: ::

        class DocumentTraceQueue(object):
            from common import Singleton
            __metaclass__ = Singleton

    """
    instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls.instance

    def clear_instance(cls):
        if cls.instance:
            del cls.instance
