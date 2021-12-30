thisset = {"apple", "banana", "cherry"}

print(thisset)

# Loop through set
for x in thisset:
    print(x)

# Check if item is in set
print("banana" in thisset)

# Add item to set
thisset.add("orange")

print(thisset)

# Add multiple items to set
thisset.update(["mango", "grapes", "kiwi"])

print(thisset)

# Get the length of the set
print(len(thisset))

# Remove item from set
thisset.remove("banana")
# Or
thisset.discard("grapes")

print(thisset)

# Remove last item in set
x = thisset.pop()

print(x)
print(thisset)
