
#프로필 이미지 전송 API#

- 프로필 이미지 전송 API 는 클라이언트에서 서버로 해당 사용자의 프로필 이미지를 업로드 하는 API이다.  


##Resource URL##
- POST : [http://qlemon.net:8000/fcal/api/account/profile/image]( http://qlemon.net:8000/fcal/api/account/profile/image )

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
| file                       | file    | 필수 | 사진파일   |
 

> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/account/profile/image

{'session_id':dGVzdEBnbWFpbC5jb207MTExMQ==, 'file':'profile.jpg'}

```


##Response(JSON-XML)##

  
| 파라미터이름     | 형식          | 필수 | 메모                                                         |
| :----------|:------------|:---|:-----------------------------------------------------------|
| meta       |     | 필수 | 메타 정보                                   |
|   msg       | string  | 필수 | 통신 관련 사항, 200 이 아닌경우, 문제의 원인 명시      |
 
 

> Response paramter 의 예:
```
{ 
    "meta": {
        "msg": "Success"
    }
}

```

**** session_id 가 없는 경우, 400 Bad Request 에러 반환. ***


**** session_id 가 잘못된  경우, 401 Unauthorized 에러 반환. ***
 

