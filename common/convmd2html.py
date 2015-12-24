# -*- coding:utf-8 -*-

def conv_md_to_html(md_text):
    """
    Convert markdown text to HTML

    :param md_text: markdown text
    :return: html
    """
    try:
        import markdown
        return markdown.markdown(md_text, extensions=["fenced_code", "tables"])
    except Exception as e:
        raise e
