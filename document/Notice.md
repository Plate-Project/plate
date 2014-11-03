
#공지사항 API#

- 공지사항 API 는 공지사항의 내용을 수신한다. 

##Resource URL##
- [http://qlemon.net:8000/fcal/api/notice]( http://qlemon.net:8000/fcal/api/notice)

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/notice
```   
 
     
##Request Parmeters##

| 파라미터이름                     | 형식             | 필수 | 메모                     |
| :------------------------- |:---------------|:---|------------------------|
| session_id                     | string    | 필수 | 세션id |
| page                     | int    | 옵션 | 요청 페이지 번호, default(1)  |
 

> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/notice?session_id=dGVzdEBnbWFpbC5jb207MTExMQ==
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
| id                     | int    | 필수 | 공지사항 번호 |
| title             | string    | 필수 | 제목          | 
| article             | string    | 필수 | 본문               | 

 

 
> Response paramter 성공의 예:
```
{
  "data": {
    "count": 1,
    "page": 1,
    "total_count": 1,
    "total_page": 1,

    "item": [
      {
        "article": "안녕하세요. 공지사항입니다.",
        "id": 1,
        "title": "공지사항입니다."
      }
    ]
  },
  "meta": {
    "msg": "Success"
  }
}

```
 
**** session_id 가 없는 경우, 400 Bad Request 에러 반환. ***


**** session_id 가 잘못된  경우, 401 Unauthorized 에러 반환. *** 