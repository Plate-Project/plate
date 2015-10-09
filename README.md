Plate
========
 
[![Pyhton2.7](https://img.shields.io/badge/python-2.7-brightgreen.svg)](https://github.com/Plate-Project/plate)  [![Pyhton3.4](https://img.shields.io/badge/python-3.4-red.svg)](https://github.com/Plate-Project/plate.git)



  
plate is the converting [Slate](http://tripit.github.io/slate) based on Ruby to Python-Flask base. And add some different functions for usages. 
  
![plate](https://farm6.staticflickr.com/5820/21503977290_41beb38dcd_b.jpg)

Example site is [here](http://ash84.net:8888)


Features
------------
(It's only differences from original [Slate](http://tripit.github.io/slate), confirm the original features at [Slate](http://tripit.github.io/slate))


- **Configuration File(config.json)**
: Set title, programming language for example codes using config.json base on JSON Format. Also set the path of the API documents and TOC(Table of contents).

- **Support Multi-API documents**
: Original [Slate](http://tripit.github.io/slate) support one API document based on Markdown format. But [plate](https://github.com/Plate-Project/plate) support multi-API documents for efficient management and amount of documents using TOC(index.json).

- **Support dynamic changes of documents**
: You can reflect the changes of API documents without restarting server. When web page refresh, if exist changes, [plate](https://github.com/Plate-Project/plate) reload API documents. Users only focus on writing API documents.

- **Make Static HTML**
: Convert Markdown(md) to Static HTML using [jinja2 template!](http://jinja.pocoo.org/).

Getting Start
------------------------------

### Support Python Version 
  - **Python, version 2.7**
  - **Python, version 3.4 or newer**

### Prerequisites
 
 - **requirements.txt** have all libraries for running plate
 - If you install using `install.py`, automatically install all libraries.

### QuickStart 

 1. Clone plate to your hard drive with `git clone https://github.com/Plate-Project/plate.git`
 2. `cd plate`
 4. Install your API document web pages using `install.py`.
 5. Start the server: `python plate.py`

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

Contributor
--------------------
plate was built by [@sh84ahn](https://twitter.com/sh84ahn) using [Slate](http://tripit.github.io/slate)

Contributing(Bugs/New Features)
--------------------
Any suggestions [submit a issue](https://github.com/Plate-Project/plate/issues).
Show me the pull requests.
