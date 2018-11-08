import json
data = '''{
  "name" : "Chuck",
  "phone" : {
	"type" : "intl",
	"number" : "+1 734 303 4456"
  },
  "email" : {
	"hide" : "yes",
  } #curly brace = like a dictionary, called object in javascript
}'''

info = json.loads(data)
print('Name:', info["name"])
print('hide:', info["email"]["hide"])