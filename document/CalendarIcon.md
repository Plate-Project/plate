
#캘린더 아이콘 받기 API#

- 캘린더 아이콘 받기 API 는 해당 캘린더에 대한 아이콘 URL을 받는 API이다.. 

##Resource URL##
- [http://qlemon.net:8000/fcal/api/calendaricon/<id>]( http://qlemon.net:8000/api/calendaricon/1 )

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/calendaricon/<id>
```   
 
     
##Request Parmeters##

본 API에서는 GET 방식의 Query String 이 아닌 URL에 캘린더ID 를 전달하는 방식으로 사용한다. 

| URL                     | 형식             | 필수 | 메모                     |
| :------------------------- |:---------------|:---|------------------------|
| id                   | int    | 필수 | 캘린더ID          |
| session_id                     | string    | 필수 | 세션id |

> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/calendaricon/1?session_id=dGVzdEBnbWFpbC5jb207MTExMQ==
```


##Response(JSON)##
 

| 파라미터이름     | 형식          | 필수 | 메모                                                         |
| :----------|:------------|:---|:-----------------------------------------------------------|
| meta       |     | 필수 | 메타 정보                                   |
|   msg       | string  | 필수 | 통신 관련 사항, 200 이 아닌경우, 문제의 원인 명시      |
| data    |  | 필수 | 데이터 정보                                                         |  
|   count    |int  | 필수 | items 내 데이터의 수                                              |  
|   item    | list | 필수 | 아이템 정보(각 API 마다 달라진다.)                                    |  
|   calendar_id       | string    | 필수 | 최신 앱 버전                                    |
|   icon_url       | string  | 필수 | 앱의 앱스토어 링크                                                       |
 

> Response paramter 의 예:
```
{
  "data": {
    "count": 1, 
    "item": [
      {
        "calendar_id": "1", 
        "icon_url": "http://icons.iconarchive.com/icons/custom-icon-design/mono-business-2/256/calendar-icon.png"
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