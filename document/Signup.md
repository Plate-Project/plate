
#회원가입 API#

- 회원가입 API 는 Fcal 서비스에 회원으로 가입하는 것이다. 

##Resource URL##
- [http://qlemon.net:8000/fcal/api/signup]( http://qlemon.net:8000/api/signup)

> API Endpoint 
```
http://qlemon.net:8000/fcal/api/signup
```   
 
     
##Request Parmeters##

| 파라미터이름                     | 형식             | 필수 | 메모                     |
| :------------------------- |:---------------|:---|------------------------|
| email                     | varchar(10)    | 필수 |   이메일 |
| password             | varchar(100)    | 필수 | 비밀번호                | 
| nickname             | varchar(100)    | 필수 | 닉네임                 | 


> Request 의 예 :


```
http://qlemon.net:8000/fcal/api/signup?email=test@gmail.com&password=1234&nickname=test
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
> Response paramter 실패의 예:
```
{
  "meta": {
    "msg": "Internal Server Error"
  }
}

```

**** 필수 파라미터가 없는 경우, 400 Invalid Parameter 에러 반환. ***


**** 이미 가입되어 있는 경우, 500 Internal Server Error 에러 반환. ***


 