
#프로필 이미지 가져오기 API#

- 프로필 이미지 전송 API 는 해당 사용자의 프로필 이미지를 가져오는 API 입니다.


##Resource URL##
- GET : [http://qlemon.net:8000/fcal/api/account/profile/image]( http://qlemon.net:8000/fcal/api/account/profile/image )

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/account/profile/image
```   

     
##Request Parmeters##
- 아래의 파라미터들은 JSON 형태로 Request Body에 실려서 전송되어야 한다. 
- session_id 에 해당하는 사용자가 전송하는 공유 캘린더의 소유자로 지정된다. 

| 파라미터이름                   | 형식             | 필수 | 메모                     |
| :------------------------- |:---------------|:---|------------------------|
| session_id                 | string    | 필수 |   세션id                     |
 

> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/account/profile/image?session_id=dGVzdEBnbWFpbC5jb207MTExMQ==

```


##Response(HTML)##
- 이미지가 페이지에 표시됨. 



**** session_id 가 없는 경우, 400 Bad Request 에러 반환. ***


**** session_id 가 잘못된  경우, 401 Unauthorized 에러 반환. ***
 

