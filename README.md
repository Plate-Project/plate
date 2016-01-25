Plate
========
 
[![Pyhton2.7](https://img.shields.io/badge/python-2.7-brightgreen.svg)](https://github.com/Plate-Project/plate)  [![Pyhton3.4](https://img.shields.io/badge/python-3.4-red.svg)](https://github.com/Plate-Project/plate.git)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/b6ab9d0d52ee42a8b2bca2c3ce5bea28)](https://www.codacy.com/app/sh84ahn/plate)
[![Build Status](https://travis-ci.org/Plate-Project/plate.svg?branch=master)](https://travis-ci.org/Plate-Project/plate)


Plate is API Documentations Tool based on Markdown(md). Convert [Slate](http://tripit.github.io/slate) based on Ruby-Middleman to Python-Flask based. And add some different functions for usages. 
  
![plate](https://farm6.staticflickr.com/5820/21503977290_41beb38dcd_b.jpg)

Example site is [plate-project.github.io](http://plate-project.github.io/). Plate document is [plate.readthedocs.org](http://plate.readthedocs.org/en/latest/index.html).


Features
------------

- **Configuration File(config.json)**
: Set a title, programming languages for example codes using `config.json` based on JSON Format. Also set the path of the API documents and TOC(Table of contents). 누구나 쉽게 설정할수 있다.  

- **Support Multi-API documents**
: [plate](https://github.com/Plate-Project/plate) support multi-API documents(multi markdown format files) for efficient management and amount of documents using TOC(index.json). 원하는 대로 
하나의 마크다운 파일에 넣고 싶으면 넣어도 되고, 아니면 API별 혹은 다른 기준에 따라서 원하는 대로 파일을 분리할 수 있다. 또한 TOC(index.json)을 통해서 각 파일들의 출력 순서를 정할 수 있다. 

- **Support dynamic changes of documents**
: Plate 는 서버모드와 정적 HTML 출력 모드를 가지고 있다. 때문에 아래의 것들이 가능하다. 
You can update the changes of API documents without restarting server. When web page refresh, if exist changes, [plate](https://github.com/Plate-Project/plate) reload API documents. Users only focus on writing API documents.


- **Make Static HTML**
: 
Convert Markdown(md) to Static HTML using [jinja2 template](http://jinja.pocoo.org/). Use this on github.io and static html service or offline.

- **Multi-Languages Searching**
: 본래 검색 기능은 lunr.js 를 기반으로 하고 있기 때문에 영어만을 검색할 수 있는데, 이를 보완하기 위해서 lunr-languages 를 
Support multi-languages searching. Use [lunr-languages](https://github.com/MihaiValentin/lunr-languages) for [supporting various languages](http://plate.readthedocs.org/en/latest/advanced.html#multi-language-search) such as Japanese, French, German etc.

- **Code Copy**
: 작성한 예제 코드를 마우스의 드래그앤 드롭 없이 쉽게 복사를 할수 있고, 그것을 이용해서 코드에 바로 적용 할수 있다. 이 기능을 제공하기 위해서 clipboard.js 를 사용하였다. 
If set <code>CLIPBOARD</code> in `config.json`, can copy codes using clicking copy link with out mouse drag and copy.


이게 엄청 쉽고, 파이썬 개발자가 아니여도 쉽게 쓸수가 있도록 구성이 되어 있다. 아래의 Getting Start 를 우선적으로 따라해봐라. 그리고 문제가 있다면 바로 알려줘. 이메일이든 
issue 게시판이든, 상관없다. 항상 이 툴은 당신을 위해서 준비가 되어 있다. 


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
    Welcome plate v0.2
    Start your API Document system.
    
    Typing API document name :<Typing your project>
    what is API document name? is "<your project>"
    
    Rename plate to  "<your project>" ...
    Complete. Enjoy developing.
    
    > cd ../<your project>
    > python plate.py
    ```

### Quick Start with Static HTML 
Start with static html: `python plate.py -m convert`
    
    > python plate.py -m convert

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
    "COPYRIGHT"          : "© 2014 plate",
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

Version v0.2.5
--------------------
- V0.2.5
    - Change basic structures
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

- pygment 
- lunr-

License
------------

Copyright 2015 Plate

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

