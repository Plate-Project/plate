slate-flask 
========
  
slate-flask is the converting [Slate](http://tripit.github.io/slate) based on Ruby to Python-Flask base. And add some different functions for usages. 
  
![slate-flask](https://farm9.staticflickr.com/8562/15916154516_b5aacc6790_c.jpg) 
 
Example site is [here](http://ash84.net:8888)


Features
------------
(It's only differences from original [Slate](http://tripit.github.io/slate), confirm the original features at [Slate](http://tripit.github.io/slate))


- **Configuration File(config.json)**
: Set title, programming language for example codes using config.json base on JSON Format. Also set the path of the API documents and TOC(Table of contents).

- **Support Multi-API documents**
: Original [Slate](http://tripit.github.io/slate) support one API document based on Markdown format. But [slate-flask](https://github.com/AhnSeongHyun/slate-flask) support multi-API documents for efficient management and amount of documents using TOC(index.json).

- **Support dynamic changes of documents**
: You can reflect the changes of API documents without restarting server. When web page refresh, if exist changes, [slate-flask](https://github.com/AhnSeongHyun/slate-flask) reload API documents. Users only focus on writing API documents.
 

Getting Start
------------------------------

### Support Python Version 
  - **Python, version 2.7**
  - **Python, version 3.4 or newer**

### Prerequisites
 
 - **requirements.txt** have all librarys for running slate-flask
 - If you install using `install.py`, automatically install all librarys. 

### QuickStart 

 1. Clone slate-flask to your hard drive with `git clonehttps://github.com/AhnSeongHyun/slate-flask.git`
 2. `cd slate-flask`
 4. Install your API document webpagse using `install.py`. 
 5. Start the server: `python slate.py`

    ```shell
    > git clone https://github.com/AhnSeongHyun/slate-flask.git
    > cd slate-flask 
    > python install.py 
    ...
    Welcome slate-flask v0.1. 
    Start your API Document system.
    
    Typing API document name :<Typing your project>
    what is API document name? is "<yout project>"
    
    Rename slate-flask to  "<yout project>" ...
    Complete. Enjoy developing.
    
    > cd ../<yout project>
    > python slate.py 
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
    "COPYRIGHT"          : "© 2014 slate-flask"
}
```

### index.json(Table of contents)
- path : ./docuemnt/index.json
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
slate-flask was built by [@sh84ahn](https://twitter.com/sh84ahn) using [Slate](http://tripit.github.io/slate)

Contributing(Bugs/New Features)
--------------------
Any suggestions [submit a issue](https://github.com/AhnSeongHyun/slate-flask/issues). 

License
--------------------
Copyright 2008-2013 Concur Technologies, Inc.  
modified by AhnSeongHyun(All python codes)

Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0


**If any probelms realated license, contact [@sh84ahn](https://twitter.com/sh84ahn).**

