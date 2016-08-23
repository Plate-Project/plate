..

Plate
=====

Introduce
---------

**Plate is API Documentations Tool based on Markdown(md)** . Convert `Slate <http://tripit.github.io/slate>`_ based on Ruby-Middleman to Python-Flask based. And add some different functions for usages.

.. image:: https://farm6.staticflickr.com/5820/21503977290_41beb38dcd_b.jpg

Example site is `plate-project.github.io <http://plate-project.github.io/>`_.


Features
------------

- **Configuration File(config.json)**
    - Set a title, programming languages for example codes using ``config.json`` based on JSON Format. Also set the path of the API documents and TOC(Table of contents). Anyone can easily set up.

- **Support Multi-API documents**
    - `plate<https://github.com/Plate-Project/plate`_ support multiple API documents(multi markdown format files) for efficient management and amount of documents. As you with, use one markdown file or separate markdown files by API or another criterion. Also you can set the output order using TOC(index.json).

- **Support dynamic changes of documents**
    - You can update the changes of API documents without restarting server. When web page refresh, if exist any changes, `plate<https://github.com/Plate-Project/plate`_ reload API documents. Users only focus on writing API documents.

- **Make Static HTML**
    - Convert Markdown(md) to Static HTML using `jinja2 template <http://jinja.pocoo.org/>`_. Use this on github.io and static html service or offline.

- **Multi-Languages Searching**
    - To `support searching various languages<http://plate.readthedocs.org/en/latest/advanced.html#multi-language-search>`_ such as Japanese, French, German, etc, use not only `lunr.js<http://lunrjs.com/>`_ but also `lunr-languages<https://github.com/MihaiValentin/lunr-languages>`_.

- **Code Copy**
    - It can be easily copy the example codes without mouse drag and drop, immediately apply this to your codes. Set ``CLIPBOARD`` in ``config.json``, can copy codes using clicking copy link.

Plate is very easy for any developers. First of all, follow below Getting Start.
And then you have any problems, immediately notify(email, issue board, anything). Always, plate is ready for you.

Getting Start
=============

Support Python Version
----------------------
- **Python, version 2.7 ~ 3.4**

Prerequisites
-------------

- **requirements.txt** have all libraries for running plate

.. literalinclude:: ../requirements.txt

- If you install using ``quick-start.py``, automatically install all libraries.
- manually, install all libraries:

.. code-block:: shell

    pip install -r requirements.txt

Quick Start with Server
-----------------------

1. Clone plate to your hard drive with ``git clone https://github.com/Plate-Project/plate.git``
2. ``cd plate``
3. Install your API document web pages using ``quick-start.py`` .
4. Start with server: ``python plate.py`` ::

    git clone https://github.com/Plate-Project/plate.git
    cd plate
    python install.py
    ...

    Welcome plate v0.2.6
    Start your API Document system.

    Typing API document name :<Typing your project>
    what is API document name? is "<your project>"

    Rename plate to  "<your project>" ...
    Complete. Enjoy developing.

    cd ../<your project>
    python plate.py


Quick Start with Static HTML
----------------------------

    Start with static html:``python pst.py -f <conf file>``

    .. code-block:: shell

        python pst.py -f config.json


Config
------

- Configuration file for Plate
- path : ``./config.json``

.. literalinclude:: ../config.json
   :language: json


====================  ===============================================
KEY                   DESCRIPTION
====================  ===============================================
PORT                  Server Port  
TITLE                 <head><title>Title String</title></head>
LOGO_IMG              Image path, Display at left top      
LOGO_TITLE            Logo Title, Display at left top, If you set ``LOGO_IMG``, do not display LOGO_TITLE.
SEARCH_ON             true or false, if true available searching 
SUPPORT_LANG          List Type, Programming Language to display example tabs
API_DOC_PATH          Directory Path include markdown API document files. 
API_DOC_INDEX_PATH    JSON format have Markdown file list.
COPYRIGHT             copy right string   
FAVICON               favicon file name in ``/static/images``
CLIPBOARD             Display copy button below codes 
STATIC                Making Static HTML Section   
  DIR                 Directory Path for saving static html.
  HTML                Static html file name.
====================  ===============================================

Usage
=====

Table of Contents
-----------------
- TOC file for setting documents order and file name.
- Set ``API_DOC_INDEX_PATH`` in ``config.json``.
- path : ``./document/index.json``

.. literalinclude:: ../document/index.json
   :language: json

TOC(Table of content) appears as written order. If index.json path is not equal API document file(md) path, must write file path.

.. image:: https://farm1.staticflickr.com/597/21701121331_01a93bcce4.jpg


Logo and Title
---------------
- You can select the logo image or title text. not **BOTH** .
- If set ``LOGO_IMG`` in config.json, display specific logo image at left-top.
- If set ``LOGO_TITLE`` in config.json, display specific title text at left-top.

.. image:: https://farm6.staticflickr.com/5834/22006576161_b2824c99f7_o.png

.. image:: https://farm1.staticflickr.com/563/21996746525_91c7ff8ea2_o.png


If you set both, ``LOGO_IMG`` only display.

.. code-block:: json

    {
        "LOGO_TITLE"         : "Management API",
        "LOGO_IMG"           : "logo.png"
    }


Emphasis Syntax
---------------
- You can the emphasis syntax for using ``<aside class="CLASSNAME">``.
- ``CLASSNAME`` is ``success`` or ``notice`` or ``warning``.

.. code-block:: html

    <aside class="warning">
        Must encrypt password using a key.
    </aside>

.. image:: https://farm1.staticflickr.com/752/23746756075_beff560049.jpg

.. code-block:: html

    <aside class="notice">
        No mandatory parameter, return 400 Invalid Parameter
    </aside>

.. image:: https://farm6.staticflickr.com/5623/23450886360_6b8b556766.jpg


.. code-block:: html

    <aside class="success">
        Success, return HTTP Status code 200 OK.
    </aside>

.. image:: https://farm6.staticflickr.com/5835/23378773719_56684cabe6.jpg
