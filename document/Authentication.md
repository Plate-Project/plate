
#Authentication#



##기본인증 방법##


- CPID, API_KEY, TIMESTAMP 를 이용한 인증 방식.

###필드설명

| 필드                         | 설명                       |
| :------------------------- |:-------------------------          |
| CPID                       | 각 CP사에 발급된 CPID               |
| API_KEY                    | CP사의 신청에 의해서 발급된 gid)    |
| TIMESTAMP                  | 현재 시간                          |



##전체 과정##

**클라이언트 과정**

1. CPID, TIMESTAMP(YYYMMDDHHNNSS), API_KEY를 구분자(;)로 연결한 문자열을 만든다.
2. SHA1 해시알고리즘(HMAC-SHA1)으로 1번 과저에서 만든 문자열의 해쉬값을 추출한다. (Signature)
3. HTTP Basic 인증을 위한 username 은 danal로 지정한다.
4. HTTP Baisc 인증을 위한 pw 는  CPID;SIGNATURE;TIMESTAMP;NONCE 를 연결한 문자열을 만든다.
5. BASE64(username:pw) 로 인코딩을 해서 HTTP Authorization 헤더에 적재한다. 


> 클라이언트 호출 예제 코드 :
```python
import datetime
from time import strftime, localtime
from hashlib import sha1
import hmac

raw = CPID + ';' + TIMESTAMP + ';' + API_KEY
signature_key = "DANAL"
signature = hmac.new(signature_key, raw, sha1).hexdigest()

username = 'DANAL'
pw = CPID + ';'+signature + ';' + TIMESTAMP

import requests
from requests.auth import HTTPBasicAuth
r = requests.get(url,auth=HTTPBasicAuth(username, pw))
```


**API 서버 과정** 

1. 서버로 들어온 요청의 헤더 부분에서 Authorization 을 가져온다. 
2. Base64 디코딩을 하고, 콜론을 제거한다. 
3. 2번의 문자열을 기존의 가지고 있는 비밀키를 이용해서 복호화를 한다. 
4. 구분자를 이용해서 API_KEY 와 TimeStamp를 분리한다. 
5. 분리된 TimeStamp가 유효한 범위내에 있는지 체크한다. (없으면 에러 반환)
6. 있으면, API_KEY 가 발급된 API_KEY 관련 DB에 있는지 확인한다. (없으면 에러 반환)
7. 있으면, 실제 해당 API 가 해야할 일을 수행하고 결과를 반환한다. 

