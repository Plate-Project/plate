# -*- coding:utf-8 -*-

def is_absolute(url):
    try:
        from urlparse import urlparse
    except ImportError as e:
        from urllib.parse import urlparse
    return bool(urlparse(url).netloc)
