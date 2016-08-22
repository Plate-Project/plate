# -*- coding:utf-8 -*-

try:
    from urllib.parse import urlparse, urlencode
except ImportError:
    from urlparse import urlparse


def is_absolute(url):

    if url:
        parsed_url = urlparse(url)
        if bool(parsed_url.netloc):
            return True
        else:
            from os.path import isabs
            return isabs(parsed_url.path)
    else:
        return False
