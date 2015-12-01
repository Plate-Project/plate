
#Signup API#
- Sign up the service using id, password

![Signup](https://farm6.staticflickr.com/5658/20891390438_0f5e639451.jpg)



##Resource URL##
- [http://127.0.0.1/api/signup]( http://127.0.0.1/api/signup )
     
##Request Parameters##

| name            | type            | mandatory | memo           | 
| :---------------|:--------------- |:----------|----------------|
| id              | string          | O         | email          |
| password        | string          | O         |                |
| nickname        | string          | O         |                | 


  
> Example

```shell
curl http://127.0.0.1/api/signin?id=test@gmail.com&password=1234 
```

 
```python
import requests
payload = {"id":"test@gmail.com", "password":"1234", "nickname":"sarada"}
r = requests.post("http://127.0.0.1/api/signup", data=payload)
```



##Response - JSON##
 

| name       | type    | mandatory | memo                                |
| :----------|:--------|:----------|:------------------------------------|
| meta       |         | O         | Meta Info                           |
| status     | int     | O         | HTTP Status Code                    |
| msg        | string  | O         | HTTP Status Message                 |
 

<aside class="notice">
No mandatory parameter, return 400 Invalid Parameter 
</aside>


<aside class="notice">
If already signup, return 500 Internal Server Error
</aside>


> Response 200 OK
```json
{
  "meta": {
    "status" : 200,
    "msg": "OK"
  }
}

```
 
> Response 500 Internal Server Error
```json
{
  "meta": {
    "status" : 500, 
    "msg": "Internal Server Error"
  }
}

```

