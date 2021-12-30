thistuple = ("apple", "banana", "cherry")

# Loop through Tuple
for x in thistuple:
    print(x)

# Check if value is present in tuple
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Find the length of the tuple
print(len(thistuple))

# Delete Tuple, will cause error because tuple no longer exists
del thistuple
print(thistuple)


