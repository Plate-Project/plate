# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''


def conv_md2html(md_text):
    import markdown
    return markdown.markdown(md_text, extensions=["fenced_code", "tables"])
