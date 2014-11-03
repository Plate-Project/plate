
#친구리스트 API#

- 친구리스트 API 는 자신의 친구 리스트를 수신한다. 

##Resource URL##
- [http://qlemon.net:8000/fcal/api/friends]( http://qlemon.net:8000/fcal/api/friends)

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/friends
```   
 
     
##Request Parmeters##

| 파라미터이름                     | 형식             | 필수 | 메모                     |
| :------------------------- |:---------------|:---|------------------------|
| session_id                     | string    | 필수 | 세션id |
| page                     | int    | 옵션 | 요청 페이지 번호, default(1)  |
 

> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/friends?session_id=dGVzdEBnbWFpbC5jb207MTExMQ==
```


##Response(JSON)##

| 파라미터이름     | 형식          | 필수 | 메모                                                         |
| :----------|:------------|:---|:-----------------------------------------------------------|
| meta       |     | 필수 | 메타 정보                                   |
|   msg       | string  | 필수 | 통신 관련 사항, 200 이 아닌경우, 문제의 원인 명시      |
| data    |  | 필수 | 데이터 정보                                                         |  
|   count    |int  | 필수 | items 내 데이터의 수                                              |  
|   page          | int    | 필수 | 요청한 페이지 번호 |
|   total_count   | int    | 필수 | 전체 데이터수      |
|   total_page    | int    | 필수 | 전체 페이지수      |
|   item    | list | 필수 | 아이템 정보(각 API 마다 달라진다.)                                    |  
| email             | string    | 필수 | 이메일          | 
| nickname             | string    | 필수 | 닉네임               | 

 

 
> Response paramter 성공의 예:
```
{
  "data": {
    "count": 2,
    "item": [
      {
        "email": "test1@gmail.com",
        "nickname": "test"
      },
      {
        "email": "test2@gmail.com",
        "nickname": "test"
      }
    ],
    "page": 1,
    "total_count": 2,
    "total_page": 1
  },
  "meta": {
    "msg": "Success"
  }
}

```
**** 친구리스트의 경우, 상호 친구 추가가 된 친구만 출력된다. ***


**** session_id 가 없는 경우, 400 Bad Request 에러 반환. ***


**** session_id 가 잘못된  경우, 401 Unauthorized 에러 반환. *** 