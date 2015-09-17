
#Signin API#
- Signin the service using id, password

![Signin](https://farm1.staticflickr.com/642/20891211720_09e70f97c7.jpg)


##Resource URL##
- [http://127.0.0.1/api/signin]( http://127.0.0.1/api/signin )

##Request Parameter##

| name            | type            | mandatory | memo           |
| :---------------|:--------------- |:----------|----------------|
| id              | string          | O         | email          |
| password        | string          | O         |                | 

<aside class="warning">
Must encrypt password using a key. 
</aside>

  
> Example

```shell
curl http://127.0.0.1/api/signin?id=test@gmail.com&password=1234 
```

```python
import requests
r = requests.get("http://127.0.0.1/api/signin?id=test@gmail.com&password=1234")
```

```java
HttpClient httpclient = new DefaultHttpClient();
HttpGet httpget = new HttpGet("http://127.0.0.1/api/signin?id=test@gmail.com&password=1234");
HttpResponse response = httpclient.execute(httpget);
```
 

##Response(JSON)##
 

| name       | type    | mandatory | memo                                |
| :----------|:--------|:----------|:------------------------------------|
| meta       |         | O         | Meta Info                           |
| status     | int     | O         | HTTP Status Code                    |
| msg        | string  | O         | HTTP Status Message                 |
 

> Response 200 OK
```
{
  "meta": {
    "status" : 200 
    "msg": "OK"
  }
}

```
 
> Response 500 Internal Server Error
```
{
  "meta": {
    "status" : 500 
    "msg": "Internal Server Error"
  }
}

```
