"""
#
# part: python JSON
#API = Application Programming Inter
#
"""  
import json

# make a JSON (String)
x = '{"name": "John", "age": 20, "city": "Phuket"}'

# parse
y =  json.loads(x)


# python dictionary
print(y)
print(type(y))
print(y["city"])

# python dictionary
a = {
    "name": "noa",
    "age": 20,
    "city": "Phuket"
}

# convert to JSON (string)
b = json.dumps(a)

#JSON String
print(b)