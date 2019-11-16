import json
#a string of json formatted data
json_data = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
#turning said string into actual json data
parsed_json = (json.loads(json_data))
#you can see that its a python dictionary now
print(json.dumps(parsed_json, indent=4, sort_keys=True))

loaded_json = json.loads(json_data)
#you can see how python now sees it, as usable data. hooray!
for x in loaded_json:
    print("%s: %d" % (x, loaded_json[x]))
