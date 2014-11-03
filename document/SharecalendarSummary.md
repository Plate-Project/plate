
#공유캘린더 카테고리 요약 API#

- 공유캘린더 카테고리 요약 API 는 카테고리 별로 10개의 공유갤린더 리스트를 반환한다. 

##Resource URL##
- [http://qlemon.net:8000/fcal/api/sharecalendar/summary]( http://qlemon.net:8000/fcal/api/sharecalendar/summary)

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/sharecalendar/summary
```   
 
     
##Request Parmeters##

| 파라미터이름                     | 형식             | 필수 | 메모                     |
| :------------------------- |:---------------|:---|------------------------|
| session_id                     | string    | 필수 | 세션id | 
 

> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/sharecalendar/summary?session_id=dGVzdEBnbWFpbC5jb207MTExMQ==
```


##Response(JSON)##

| 파라미터이름     | 형식          | 필수 | 메모                                                         |
| :----------|:------------|:---|:-----------------------------------------------------------|
| meta       |     | 필수 | 메타 정보                                   |
|   msg       | string  | 필수 | 통신 관련 사항, 200 이 아닌경우, 문제의 원인 명시      |
| data    |  | 필수 | 데이터 정보                                                         |  
|   count    |int  | 필수 | items 내 데이터의 수                                              |  
|   item    | list | 필수 | 아이템 정보(각 API 마다 달라진다.)                                    |  
|     category   | string    | 필수 | 카테고리 |
|     count             | int    | 필수 | 카테고리내 공유캘린더의 수          | 
|     calendar_list             | list    | 필수 | 공유캘린더 리스트                | 
|       calendar   | string    | 필수 | 공유캘린더 xml 문서 |
|       id             | int    | 필수 | 공유캘린더 ID      | 

 

 
> Response paramter 성공의 예:
```
 {
  "data": {
    "count": 2,
    "item": [
      {
        "category": 1,
        "count": 2,
        "calendar_list": [
          {
            "calendar": xml string,
            "id": 1
          },
          {
            "calendar": xml string,
            "id": 2
          }
        ]
      },
      {
        "category": 2,
        "count": 2,
        "calendar_list": [
          {
            "calendar": xml string,
            "id": 4
          },
          {
            "calendar": xml string,
            "id": 5
          }
        ]
      }
    ]
  }
}


```
 
**** session_id 가 없는 경우, 400 Bad Request 에러 반환. ***

**** session_id 가 잘못된  경우, 401 Unauthorized 에러 반환. *** 