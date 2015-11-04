# -*- coding:utf-8 -*-

def conv_md2html(md_text):
    """
    Convert markdown text to HTML

    :param md_text: markdown text
    :return: html
    """
    import markdown
    return markdown.markdown(md_text, extensions=["fenced_code", "tables"])
