# -*- coding:utf-8 -*-


from pygments import highlight
from pygments import lexers
from pygments.formatters import HtmlFormatter


def syntax_highlight(lang, code):
    """
    code highlighting HTML Format

    :param lang: programming language
    :param code: code(not html)
    :return: highlighted code(html format)
    """

    try:
        lexer = lexers.get_lexer_by_name(lang.lower())
        highlighted = highlight(code, lexer, HtmlFormatter())

        splitted = highlighted.split('"highlight')
        highlighted = splitted[0] + '"highlight ' + lang + splitted[1]

        highlighted = highlighted.replace("<pre>", "")
        highlighted = highlighted.replace("</pre>", "")
        highlighted = highlighted.replace("div", "pre")

        return highlighted
    except Exception as e:
        raise e
