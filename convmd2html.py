# -*- coding:utf-8 -*-
'''
Created on 2014. 8. 19.
@author: seonghyunan
'''

import markdown
import codecs

def conv_md2html(md_text):
    return markdown.markdown(md_text, extensions=["fenced_code", "tables"])
