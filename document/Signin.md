
#Signin API#
- Signin the service using id, password

##Resource URL##
- [http://127.0.0.1/api/signin]( http://127.0.0.1/api/signin )

##Request Parameter##

| name            | type            | mandatory | memo           |
| :---------------|:--------------- |:----------|----------------|
| id              | string          | O         | email          |
| password        | string          | O         |                | 


  
> Example

```shell
curl http://127.0.0.1/api/signin?id=test@gmail.com&password=1234 
```

 
```python
import requests
r = requests.get("http://127.0.0.1/api/signin?id=test@gmail.com&password=1234")
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
