#Notice.jp API#

- 通知データベースからの通知を取得します。

##リソースのURL##
- [http://qlemon.net:8000/fcal/api/notice]( http://qlemon.net:8000/fcal/api/notice)


> APIエンドポイント
```
http://qlemon.net:8000/fcal/api/notice
```
 
     
##リクエストParameters##

|名前|タイプ|必須|メモ|
| :------------------------- |:---------------|:---|------------------------| 
| page                     | int    | オプション | ページ番号、デフォルト（1） |
 
 
<aside class="notice">
ページがゼロ（0）の場合、内部で1にページを設定します。
</aside>



>リクエスト例：


```bash
curl http://127.0.0.1/notice?page=1
```
 
```python
import requests
r = requests.get("http://127.0.0.1/notice?page=1")
```

```java
HttpClient httpclient = new DefaultHttpClient();
HttpGet httpget = new HttpGet("http://127.0.0.1/notice?page=1");
HttpResponse response = httpclient.execute(httpget);
```



##レスポンス- JSON##

|名前|タイプ|必須|メモ|
| :------------------------- |:---------------|:---|------------------------| 
| meta       |     | 必要 | メタ情報                                   |
| msg       | string  | 必要 | http status messsage, if not 200 OK.      |
| data    |  | 必要 |  ペイロード                                                        |  
|   count    |int  | 必要 | アイテムの数                                             |  
|   page          | int    | 必要 | リクエストページ番号 |
|   total_count   | int    | 必要 | 総データ数    |
|   total_page    | int    | 必要 | total page count  |
|   item    | list | 必要 |                                     |  
| id                     | int    | 必要 | notice number(sequence) |
| title             | string    | 必要 | タイトル        | 
| article             | string    | 必要 | body               | 
| type             | int    | 必要 | type             | 
| icon_type             | int    | 必要 | icon type               | 
| date            | datetime    | 必要 | datetime             | 
 
 
> Response paramter Example:
```json
{
  "data": {
    "count": 1,
    "item": [
      {
        "article": "Hello",
        "date": 201509091530,
        "icon_type": 0,
        "id": 1,
        "title": "体験版のお知らせ",
        "type": 0
      }
    ],
    "page": 1,
    "total_count": 1,
    "total_page": 1
  },
  "meta": {
    "msg": "Success"
  }
}

``` 