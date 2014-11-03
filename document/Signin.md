
#로그인 API#

- 로그인 API 는 회원이 가입되어 있는 상태에서 앱의 정보와 함께 회원의 세션ID 를 가져오는것을 목적으로 함. 

##Resource URL##
- [http://qlemon.net:8000/fcal/api/signin]( http://qlemon.net:8000/api/signin )

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/signin
```   
 
     
##Request Parmeters##

| 파라미터이름                     | 형식             | 필수 | 메모                     |
| :------------------------- |:---------------|:---|------------------------|
| os                     | varchar(10)    | 필수 |   앱의 타입(ios | android)                     |
| id                   | varchar(100)    | 필수 | email 형식 id          |
| password             | varchar(100)    | 필수 | 비밀번호                | 


> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/signin?os=ios&id=test@gmail.com&password=1111
```


##Response(JSON)##
 

| 파라미터이름     | 형식          | 필수 | 메모                                                         |
| :----------|:------------|:---|:-----------------------------------------------------------|
| meta       |     | 필수 | 메타 정보                                   |
|   msg       | string  | 필수 | 통신 관련 사항, 200 이 아닌경우, 문제의 원인 명시      |
| data    |  | 필수 | 데이터 정보                                                         |  
|   count    |int  | 필수 | items 내 데이터의 수                                              |  
|   item    | list  | 필수 | 아이템 정보(각 API 마다 달라진다.)                                    |  
|   app_version       | string    | 필수 | 최신 앱 버전                                    |
|   app_link       | string  | 필수 | 앱의 앱스토어 링크                                                       |
|   session_id    | string | 필수 | 세션ID                                                        |  
 

> Response paramter 의 예:
```
{
  "data": {
    "count": 1, 
    "item": 
    [
        {
            "app_link": "http://naver.com", 
            "app_version": "1.0.0", 
            "session_id": "dGVzdEBnbWFpbC5jb207MTExMQ=="
        }
    ]
  }, 
  "meta": {
    "msg": "Success"
  }
}

```

**** id/pw 가 없는 경우, 401 Unauthorized 에러 반환. ***


**** id/pw 가 맞지 않는 경우, 401 Unauthorized 에러 반환. ***


**** os 가 맞지 않는 경우, 500 Internal Server Error 에러 반환. ***
