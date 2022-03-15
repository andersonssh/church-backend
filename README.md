# site-igreja-backend
Backend do site adventistaslagoadocarneiro.com.br

## Resumo do projeto
Esta API ficará responsável pelo QUIZ da igreja e pelos dados de cada membro do clube de desbravadores.
Cada membro inscrito no clube automáticamente já participa do ranking de pontos.

## ENDPOINTS:

**/ranking** GET

**/members** GET POST PUT 

## REQUISIÇÕES

**GET /ranking**

Retorna o ranking de membros em ordem decrescente com base na pontuação.


```
{
    'data': [
       ('')
    ]
}
```

**GET /members**

Retorna todos os dados de todos os membros cadastrados.

## RESPOSTAS

### /RANKING
**GET /ranking** 

status_code **200**

```
{
    "ranking": [
        ("name1", points), ("name2", points), ...
    ]
}
```
**POST /members** 

status_code **201**
```
{
    "document_id": "ObjectIdInSTR",
    "created_at": "date"
}
```
**PUT /members** 

status_code **200**
```
{
    "updated_at": "date"
} 
```

status_code **404**
```
{
    "error": "member not found"
}
```

### /MEMBERS
**GET /members** 

status_code **200**

```
{
    "<UniqueValueObjectIdInString>": {
        "name": "jose",
        "role": "capelao",
        "points": 300
    },
    "<UniqueValueObjectIdInString>": {
        "name": "maria",
        "role": "secretária",
        "points": 500
    }, 
    ...
}
```




