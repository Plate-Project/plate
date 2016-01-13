#Notice.fr API#

- Obtenez un avis de préavis base de données.

## Ressource URL ##
- [Http://qlemon.net:8000/fcal/api/notice](http://qlemon.net:8000/fcal/api/notice)

> Endpoint API
```
http://qlemon.net:8000/fcal/api/notice
```
 
     
##Demander Parmeters##

| Nom | Type | obligatoire | mémo |
| : ------------------------- |: --------------- |: --- | - ----------------------- |
| page | int | Option | Numéro de page, par défaut (1) |
 

<aside class = "notice">
Si la page est zéro (0), définie en interne page 1.
</aside>



> Demande Exemple:


```shell
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



##Réponse - JSON##

| Nom | Type | obligatoire | mémo |
| : ------------------------- |: --------------- |: --- | - ----------------------- |
| méta | | nécessaire | méta info |
| msg | chaîne | nécessaire | état http messsage, sinon 200 OK. |
| data | | nécessaire | charge |
| compter | int | nécessaire | nombre d'éléments |
| page | int | nécessaire | la page demande Nombre |
| total_count | int | nécessaire | nombre total de données |
| total_page | int | nécessaire | nombre total de pages |
| article | Liste | nécessaire | |
| id | int | nécessaire | préavis nombre (séquence) |
| Titre | chaîne | nécessaire | Titre |
| article | chaîne | nécessaire | corps |
| Type | int | nécessaire | Type |
| icon_type | int | nécessaire | type d'icône |
| date | datetime | nécessaire | datetime |

 
> Paramètre Réponse Exemple:
```json
{
  "data": {
    "compter": 1,
    "item": [
      {
        "article": "Bonjour",
        "date": 201509091530,
        "icon_type": 0,
        "id": 1,
        "Titre": "Avis de procès",
        "type": 0
      }
    ],
    "page": 1,
    "total_count": 1,
    "total_page": 1
  },
  "méta": {
    "msg": "Success"
  }
}

``` 