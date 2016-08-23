Plate
========

[![Pyhton2.7](https://img.shields.io/badge/python-2.7-brightgreen.svg)](https://github.com/Plate-Project/plate)  [![Pyhton3.4](https://img.shields.io/badge/python-3.4-red.svg)](https://github.com/Plate-Project/plate.git)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/b6ab9d0d52ee42a8b2bca2c3ce5bea28)](https://www.codacy.com/app/sh84ahn/plate)
[![Build Status](https://travis-ci.org/Plate-Project/plate.svg?branch=master)](https://travis-ci.org/Plate-Project/plate)
[![Code Climate](https://codeclimate.com/github/Plate-Project/plate/badges/gpa.svg)](https://codeclimate.com/github/Plate-Project/plate)



Plate is API Documentations Tool based on Markdown(md). Convert [Slate](http://tripit.github.io/slate) based on Ruby-Middleman to Python-Flask based. And add some different functions for usages.

![plate](https://farm6.staticflickr.com/5820/21503977290_41beb38dcd_b.jpg)

Example site is [plate-project.github.io](http://plate-project.github.io/). Plate document is [plate.readthedocs.org](http://plate.readthedocs.org/en/latest/index.html).


Features
------------

- **Configuration File(config.json)**
: Set a title, programming languages for example codes using `config.json` based on JSON Format. Also set the path of the API documents and TOC(Table of contents). Anyone can easily set up.

- **Support Multi-API documents**
: [plate](https://github.com/Plate-Project/plate) support multiple API documents(multi markdown format files) for efficient management and amount of documents. As you with,
use one markdown file or separate markdown files by API or another criterion. Also you can set the output order using TOC(index.json).

- **Support dynamic changes of documents**
: You can update the changes of API documents without restarting server. When web page refresh, if exist any changes, [plate](https://github.com/Plate-Project/plate) reload API documents. Users only focus on writing API documents.


- **Make Static HTML**
:
Convert Markdown(md) to Static HTML using [jinja2 template](http://jinja.pocoo.org/). Use this on github.io and static html service or offline.

- **Multi-Languages Searching**
: To [support searching various languages](http://plate.readthedocs.org/en/latest/advanced.html#multi-language-search) such as Japanese, French, German, etc, use not only [lunr.js](http://lunrjs.com/) but also [lunr-languages](https://github.com/MihaiValentin/lunr-languages).

- **Code Copy**
: It can be easily copy the example codes without mouse drag and drop, immediately apply this to your codes. Set <code>CLIPBOARD</code> in `config.json`, can copy codes using clicking copy link.


Plate is very easy for any developers. First of all, follow below **Getting Start**. And then you have any problems, immediately notify(email, issue board, anything). Always, plate is ready for you.


Getting Start
------------------------------

### Support Python Version
  - **Python, version 2.7 ~ 3.4**

### Prerequisites

 - **requirements.txt** have all libraries for running plate
 - If you install using `quick-start.py`, automatically install all libraries.

### Quick Start with Server

 1. Clone plate to your hard drive with `git clone https://github.com/Plate-Project/plate.git`
 2. `cd plate`
 3. Install your API document web pages using `quick-start.py`.
 4. Start with server: `python plate.py`

    ```shell
    > git clone https://github.com/Plate-Project/plate.git
    > cd plate
    > python install.py
    ...
    Welcome plate v0.2.6
    Start your API Document system.

    Typing API document name :<Typing your project>
    what is API document name? is "<your project>"

    Rename plate to  "<your project>" ...
    Complete. Enjoy developing.

    > cd ../<your project>
    > python plate.py
    ```

### Quick Start with Static HTML
Start with static html: `python pst.py -f <conf file>`

    > python pst.py -f config.json

### config.json(configuration file)
- path : ./config.json
```json
{
    "PORT"               : 8888,
    "TITLE"              : "API Document",
    "LOGO_TITLE"         : "API Document",
    "SEARCH_ON"          : true,
    "SUPPORT_LANG"       : ["shell", "python"],
    "API_DOC_PATH"       : "./document",
    "API_DOC_INDEX_PATH" : "index.json",
    "COPYRIGHT"          : "© 2016 plate",
    "FAVICON"            : "favicon.ico",
    "CLIPBOARD"          : true,
    "STATIC" : {
        "DIR" : "./plate_static",
        "HTML" : "index.html"
    }
}
```

### index.json(Table of contents)
- path : ./document/index.json
```json
{
    "ORDER":
    [
        "Introduction.md",
        "Signup.md",
        "Signin.md"
    ]
}
```

Version v0.2.6
--------------
- V0.2.6
    - Add Test Cases.
- V0.2.5
    - Change basic structures
    - Add Unit Testing
- v0.2.4
    - Apply Sphinx documentation


More Info
--------------------
More Information such as example, usage, internal, advanced is here. [plate.readthedocs.org](http://plate.readthedocs.org/en/latest/index.html)



Contributing
--------------------
Any suggestions [submit a issue](https://github.com/Plate-Project/plate/issues).
Show me the pull requests.


Special Thanks
-----------------
- [slate](https://github.com/tripit/slate)
- [pygments](http://pygments.org/)
- [lunr-languages](https://github.com/MihaiValentin/lunr-languages)

License
------------

Copyright 2016 Plate

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
