slate-flask 
========
  
slate-flask is the converting [Slate](http://tripit.github.io/slate) based on Ruby to Python-Flask base. And add some different functions for usages. 
  
![slate-flask](https://farm9.staticflickr.com/8562/15916154516_b5aacc6790_c.jpg) 
 
Example site is [here](http://ash84.net/slate-flask)


Features
------------
(It's only differences from original [Slate](http://tripit.github.io/slate), confirm the original features at [Slate](http://tripit.github.io/slate))


- **설정파일(config.json)**
: JSON 기반의 설정 파일을 통해서 TITLE 을 지정할수 있고, 예제 프로그래밍 언어를 설정할수 있다. 또한 API 문서의 위치와 목차 파일을 지정할수가 있다. 

- **멀티 API 도큐먼트 시스템 지원**
: 기존의 SLATE 는 하나의 MARKDOWN 기반의 API 문서를 지원한다. 그러나 slate-flask 에서는 API 문서의 양과 효율적인 관리를 위해서 목차를 통해서 여러 마크다운 기반의 API 문서를 사용할수 있도록 지원한다. 

- **문서내용 변경 동적 반영**
: 문서의 변경을 서버를 재시작 하지 않고 반영할수 있다. 다음 새로고침시 수정된 문서를 다시 로드해서 보여주기 떄문에 사용자는 오직 markdown 기반의 API 문서 작성만 신경쓰면 된다. 
 

 

Getting Start
------------------------------

### Support Python Version 
  - **Python, version 2.7 or newer**

### Prerequisites
 
 - **requirements.txt** have all librarys for running slate-flask
 - If you install using `install.py`, automatically install all librarys. 

### QuickStart 

 1. Clone slate-flask to your hard drive with `git clonehttps://github.com/AhnSeongHyun/slate-flask.git`
 2. `cd slate-flask`
 4. Install your API document webpagse using `install.py`. 
 5. Start the server: `python slate.py`
     
     

      
    ```
    > git clone https://github.com/AhnSeongHyun/slate-flask.git
    > cd slate-flask 
    > python install.py 
    ...
    Welcome slate-flask v0.1. 
    Let's start your API Document system.
    
    Typing API document name :<Typing your project>
    what is API document name? is "<yout project>"
    
    Rename slate-flask to  "<yout project>" ...
    Complete. Enjoy developing.
    
    > cd ../<yout project>
    > python slate.py 
    ```




Bugs/New Features
--------------------
Just [submit a issue](https://github.com/AhnSeongHyun/slate-flask/issues). 


