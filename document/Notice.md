
#Notice API#

- Get notice from notice database.

##Resource URL##
- [http://qlemon.net:8000/fcal/api/notice]( http://qlemon.net:8000/fcal/api/notice)

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/notice
```   
 
     
##Request Parmeters##

| name            | type            | mandatory | memo           | 
| :------------------------- |:---------------|:---|------------------------| 
| page                     | int    | option | Page Number, default(1)  |
 
<aside class="notice">
If page is zero(0), internally set page to 1. 
</aside>



> Request Example:


```shell
curl http://127.0.0.1/notice?page=1
```
 
```python
import requests
r = requests.get("http://127.0.0.1/notice?page=1")
```

```java
HttpClient httpclient = new DefaultHttpClient();
HttpGet httpget = new HttpGet("http://127.0.0.1/notice?page=1");
HttpResponse response = httpclient.execute(httpget);
```



##Response - JSON##

| name            | type            | mandatory | memo           | 
| :------------------------- |:---------------|:---|------------------------| 
| meta       |     | required | meta info                                   |
| msg       | string  | required | http status messsage, if not 200 OK.      |
| data    |  | required |  payload                                                        |  
|   count    |int  | required | count of items                                             |  
|   page          | int    | required | request page number |
|   total_count   | int    | required | total data count    |
|   total_page    | int    | required | total page count  |
|   item    | list | required |                                     |  
| id                     | int    | required | notice number(sequence) |
| title             | string    | required | title        | 
| article             | string    | required | body               | 
| type             | int    | required | type             | 
| icon_type             | int    | required | icon type               | 
| date            | datetime    | required | datetime             | 

 
> Response paramter Example:
```json
{
  "data": {
    "count": 1,
    "item": [
      {
        "article": "Hello",
        "date": 201509091530,
        "icon_type": 0,
        "id": 1,
        "title": "시험버전 공지사항",
        "type": 0
      }
    ],
    "page": 1,
    "total_count": 1,
    "total_page": 1
  },
  "meta": {
    "msg": "Success"
  }
}

``` 