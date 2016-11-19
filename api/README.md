#BACKEND 4 LYFE
`GET /search` proxies query to elasticsearch
sample params:
```q=keyword:franklin roosevelt
q=dinosaur```

sample response:
```{
    'results': [{
        'keyword': 'franklin roosevelt',
        'doc_type': 'person',
    },
    {
        'keyword': 'a cool exhibition name',
        'doc_type': 'exhibition',
    }]
}
```
** these documents will contain more fields, but they will contain at minimum
the fields keyword and doc_type

`GET /keywords` returns a list of all the keywords in elasticsearch
sample response:
```{
    'results': ['franklin roosevelt', 'a cool exhibition name']
}