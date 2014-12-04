# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

import markdown

def conv_md2html(md_text):
    return markdown.markdown(md_text, extensions=["fenced_code", "tables"])
