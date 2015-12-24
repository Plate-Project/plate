..

Internal
========


Basic Structure
---------------

.. image:: https://farm6.staticflickr.com/5775/22399136477_19138464b0_b.jpg

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

    def conv_md_to_html(md_text):
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


For monitoring the modification of API Documents, use `wachdog <https://pypi.python.org/pypi/watchdog>`_ .
After the server start, the watchdog start and monitor all documents in ``API_DOC_PATH`` of ``config.json`` .
When the server stop, also the watchdog stop. In this process, use method ``watchdocs.watch_api_doc.start_watch`` and ``watchdocs.watch_api_doc.stop_watch`` .


If raise any modification fo files, run ``watchdocs.document_trace_handler.on_modified`` method.
In this method, enqueue a event about the modification of any file to ``document_trace_queue`` .
It is a instance of ``DocumentTraceQueue`` singleton class.

And then, receive new request from user, Plate check ``document_trace_queue`` whether a event exist or not.
If any event in queue, Plate load all API Documents and convert to html.
