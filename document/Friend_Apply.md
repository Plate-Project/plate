
#친구 신청 API#

- 친구 신청 API 는 본인이 다른사용자에게 친구를 신청하는 API이다.  

##Resource URL##
- POST : [http://qlemon.net:8000/fcal/api/friends/apply]( http://qlemon.net:8000/fcal/api/friends/apply)

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/friends/apply
```   
 
     
##Request Parmeters##

| 파라미터이름                     | 형식             | 필수 | 메모                     |
| :------------------------- |:---------------|:---|------------------------|
| session_id                     | string    | 필수 | 세션id |
| friend_id                     | int    | 옵션 | 친구id(email 아님)  |
 

> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/friends/apply

{'session_id':dGVzdEBnbWFpbC5jb207MTExMQ==, 'friend_id':10}


```


##Response(JSON)##

| 파라미터이름     | 형식          | 필수 | 메모                                                         |
| :----------|:------------|:---|:-----------------------------------------------------------|
| meta       |     | 필수 | 메타 정보                                   |
|   msg       | string  | 필수 | 통신 관련 사항, 200 이 아닌경우, 문제의 원인 명시      |

 

 
> Response paramter 성공의 예:
```
{
    "meta": {
        "msg": "Success"
    }
}

```


**** session_id 가 없는 경우, 400 Bad Request 에러 반환. ***


**** session_id 가 잘못된  경우, 401 Unauthorized 에러 반환. *** 