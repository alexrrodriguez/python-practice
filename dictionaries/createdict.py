thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Access value
x = thisdict["model"]
print(x)

# Change value
thisdict["year"] = 2018
print(thisdict)

# loop through dictionary print keys
for x in thisdict:
    print(x)

# loop through dictionary print Values
for x in thisdict:
    print(thisdict[x])

# Or

# Use values function to print values
for x in thisdict.values():
    print(x)

# Loop through both key and value using items() function
for x, y in thisdict.items():
    print(x, y)

# Check if Key exists
if "model" in thisdict:
    print("Yes, 'model' is a key in the thisdict dictionary")

# Get the length of dictionary
print(len(thisdict))

# Add item to dictionary
thisdict["color"] = "red"
print(thisdict)

# remove an item from dictionary
thisdict.pop("model")
print(thisdict)
