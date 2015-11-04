..

Internal
========


Basic Structure
---------------

.. image:: https://farm1.staticflickr.com/766/22723449391_5d8b94111a_o.png

Internally, Plate have **3 steps** :

- Get API Document
- Convert markdown to HTML
- Highlight code according to programming languages



**1. Get API Document**

- Read markdown from API Document based on markdown format using ``API_DOC_PATH`` and ``API_DOC_INDEX_PATH`` in ``config.json``.
- Sort by ``index.json`` of ``API_DOC_INDEX_PATH``.

**2. Convert markdown to HTML**

- Convert markdown to HTML using `markdown python module <https://pypi.python.org/pypi/Markdown>`_
- Use markdown extensions :
  - fence_codes : markdown code block to html pre tag
  - tables : markdown table syntax to html table tag

.. code-block:: python

    def conv_md2html(md_text):
        import markdown
        return markdown.markdown(md_text, extensions=["fenced_code", "tables"])


**3. Highlight code according to programming languages**

- Use `pygemnts <http://pygments.org/>`_ for highlighting codes
- Support various programming languages and markup.

.. code-block:: python

    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.lexers import JavaLexer
    from pygments.formatters import HtmlFormatter

    highlighted = highlight(code, PythonLexer(), HtmlFormatter())
    highlighted = highlight(code, JavaLexer(), HtmlFormatter())


Realtime monitoring API Document
--------------------------------

.. image:: https://farm6.staticflickr.com/5740/22089514844_4088d51454_o.png