"""import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)          #json to python dictionary
print(y["age"]) """

import json
x={"gadgets":["powerbanks","watch","hard disk"],"electronics":"tv's","year":2014}      #python to json
print(json.dumps(x,indent=2,sort_keys=True))







