
#공유캘린더 전송 API#

- 공유캘린더 전송 API 는 클라이언트에서 서버로 XML 기반의 공유캘린더 문서를 전송하는것을 목적으로 한다. 

##Resource URL##
- POST : [http://qlemon.net:8000/fcal/api/sharecalendar]( http://qlemon.net:8000/fcal/api/sharecalendar )

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/sharecalendar
```   

     
##Request Parmeters##
- 아래의 파라미터들은 JSON 형태로 Request Body에 실려서 전송되어야 한다. 
- session_id 에 해당하는 사용자가 전송하는 공유 캘린더의 소유자로 지정된다. 

| 파라미터이름                     | 형식             | 필수 | 메모                     |
| :------------------------- |:---------------|:---|------------------------|
| session_id                     | string    | 필수 |   세션id                     |
| calendar                     | string    | 필수 | 공유캘린더 XML 문서   |
 

> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/sharecalenda

{'session_id':dGVzdEBnbWFpbC5jb207MTExMQ==, 'calendar':'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<QLShareCalendar xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">...'}

```


##Response(JSON-XML)##
- 전송완료시, 추가된 공유캘린더의 id가 리턴된다. 


| 파라미터이름     | 형식          | 필수 | 메모                                                         |
| :----------|:------------|:---|:-----------------------------------------------------------|
| meta       |     | 필수 | 메타 정보                                   |
|   msg       | string  | 필수 | 통신 관련 사항, 200 이 아닌경우, 문제의 원인 명시      |
| data    |  | 필수 | 데이터 정보                                                         |  
|   count    |int  | 필수 | items 내 데이터의 수                                              |  
|   item    | list | 필수 | 아이템 정보(각 API 마다 달라진다.)                                    |  
|   share_calendar_id    | string |  필수 | 추가된 공유캘린더 ID                                    |  
  

 

> Response paramter 의 예:
```
{
    "data": {
        "count": 1,
        "item": [
            {
                "share_calendar_id": 71
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


**** calendar 가 없는 경우, 400 Bad Request 에러 반환. ***


**** calendar 가 추가되지 못한 경우, 500 Internal Server Error 에러 반환. ***



