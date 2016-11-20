#BACKEND 4 LYFE
##Using the API
`GET /search` proxies query to elasticsearch
sample params:
```
q=keyword:Akeley, Carl Ethan, 1864-1926
```

sample response:
```
{
    "results": [{
        "keyword": "Akeley, Carl Ethan, 1864-1926",
    
        "description": "Carl Ethan Akeley (born May 19, 1864, Clarendon, New York— died November 17, 1926, Belgian Congo, Africa), taxidermist, sculptor, inventor, explorer, and naturalist, who led five expeditions to Africa, three of which for the Museum of Natural History where he gathered specimens for his African Hall Exhibition. He is the author of the book In Brightest Africa...",

        "doc_type": "person"
    }]
}
```

sample params:
```
q=akeley
```

sample response:
```
{
    "results": [{
        "keyword": "Akeley, Carl Ethan, 1864-1926",
    
        "description": "Carl Ethan Akeley (born May 19, 1864, Clarendon, New York— died November 17, 1926, Belgian Congo, Africa), taxidermist, sculptor, inventor, explorer, and naturalist, who led five expeditions to Africa, three of which for the Museum of Natural History where he gathered specimens for his African Hall Exhibition. He is the author of the book In Brightest Africa...",

        "doc_type": "person"
    },
    {
        "keyword": "Akeley-Eastman-Pomeroy African Hall Expedition of the American Museum of Natural History",

        "description": "The Akeley-Eastman-Pomeroy African Hall Expedition was a collecting expedition to Africa; its mission was to provide specimens for the African Hall at the American Museum of Natural History, originally conceived in 1910. The man behind both the exhibit hall and the expedition was Carl Ethan Akeley, an animal sculptor and taxidermist, an inventor, naturalist and photographer. The Eastman-Pomeroy expedition focused on collecting specimens for the dioramas of the African Hall, as well as accessories such as grass and bushes, and the creation of background paintings from artists William Leigh and Arthur August Jansson...",

        "doc_type": "expedition"
    }]
}
```

`GET /keywords` returns a list of all the keywords in elasticsearch
sample response:
```
{
    'results': ['franklin roosevelt', 'a cool exhibition name']
}
```

##Setting up the dev environment
Setting up the virtual environment:
```
$ cd api
$ virtualenv venv
$ source venv/bin/activate
```

Setting up elasticsearch:
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew install elasticsearch
$ brew services start elasticsearch
```

Running the API:
```
$ pip install -r requirements.txt
$ python ./metasearch.py
```
