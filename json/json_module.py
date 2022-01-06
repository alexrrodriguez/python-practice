import json

# some json
x = '{"name": "John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a python dictionary
print(y["age"])

# convert from python to JSON

# a python object(dictionary)
x = {"name": "John", "age": 30, "city": "New York"}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string
print(y)

# convert python objects to JSON strings
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# convert single python object into JSON string
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# convert into JSON
y = json.dumps(x)

# result is a JSON string:
print(y)

# use four indents to make it easier to read JSON results
print(json.dumps(x, indent=4))

# use . and a space to seperate objects and use a space and = with another space to seperate keys from thier values
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# sort the result alphabetically by keys
print(json.dumps(x, indent=4, sort_keys=True))
