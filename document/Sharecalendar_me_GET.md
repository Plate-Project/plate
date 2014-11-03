
#내 공유캘린더 가져오기 API#

- 내 공유캘린더 가져오기 API 는 내 소유의 공유 캘린더를 가져오는 것을 목적으로 한다. 

##Resource URL##
- GET : [http://qlemon.net:8000/fcal/api/sharecalendar/me]( http://qlemon.net:8000/fcal/api/sharecalendar/me )

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/sharecalendar/me
```   
 
     
##Request Parmeters##

| 파라미터이름                     | 형식             | 필수 | 메모         |
| :------------------------- |:---------------|:---|------------------------|
| session_id                     | string    | 필수 |   세션id              |
| page                     | int    | 옵션 | 요청 페이지 번호, default(1)  |
 

> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/sharecalendar/me?session_id=dGVzdEBnbWFpbC5jb207MTExMQ==
```


##Response(JSON-XML)##
- 공유캘린더 리스트는 JSON을 기반으로 하나 공유캘린더 자체는 XML 문서로 전달된다. 


| 파라미터이름     | 형식          | 필수 | 메모                                                         |
| :----------|:------------|:---|:-----------------------------------------------------------|
| meta       |     | 필수 | 메타 정보                                   |
|   msg       | string  | 필수 | 통신 관련 사항, 200 이 아닌경우, 문제의 원인 명시      |
| data    |  | 필수 | 데이터 정보                                                         |  
|   count    |int  | 필수 | items 내 데이터의 수                                              |  
|   page    | int    | 필수  | 요청한 페이지 번호 |
|   total_count   | int    | 필수 | 전체 데이터수  |
|   total_page    | int    | 필수 | 전체 페이지수  |
|   text    | string    | 옥션 | 입력한 검색어(입력한 경우에 한해서)  |
|   item    | list | 필수 | 아이템 정보(각 API 마다 달라진다.)                                    |  
|     id    | string |  필수 |  캘린더 ID                                    |  
|     calendar    | XML |필수   | 캘린더 문서                                    |  

 

> Response paramter 의 예:
```
{
  "data": {
    "count": 2, 
    "page": 1,
    "total_count": 2,
    "total_page": 1,
    "item": [
      {
        "calendar": "XML", 
        "id": "123dsef"
      }, 
      {
        "calendar": "XML", 
        "id": "123dse3"
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


