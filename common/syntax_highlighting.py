# -*- coding:utf-8 -*-
'''
Created on 2014. 12. 03
@author: AhnSeongHyun
'''

from pygments import highlight
from pygments.lexers import *
from pygments.formatters import HtmlFormatter


def syntax_highlight(lang, code):
    #print "lang : " + lang +"    code : " + code
    highlighted = None

    if lang.lower() == 'python':
        highlighted = highlight(code, PythonLexer(), HtmlFormatter())

    elif lang.lower() == 'shell':
        highlighted = highlight(code, BashLexer(), HtmlFormatter())

    elif lang.lower() == 'asp':
        highlighted = highlight(code, CSharpAspxLexer(), HtmlFormatter())

    elif lang.lower() == 'csharp':
        highlighted = highlight(code, CSharpLexer(), HtmlFormatter())

    elif lang.lower() == 'ruby':
        highlighted = highlight(code, RubyLexer(), HtmlFormatter())

    elif lang.lower() == 'json':
        highlighted = highlight(code, JsonLexer(), HtmlFormatter())
        
    elif lang.lower() == 'js':
        highlighted = highlight(code, JavascriptLexer(), HtmlFormatter())
    
    elif lang.lower() == 'objective-c':
        highlighted = highlight(code, ObjectiveCLexer(), HtmlFormatter())



    splitted = highlighted.split('"highlight')
    highlighted = splitted[0] + '"highlight '+lang + splitted[1]

    highlighted = highlighted.replace("<pre>","")
    highlighted = highlighted.replace("</pre>","")
    highlighted = highlighted.replace("div","pre")

    return highlighted