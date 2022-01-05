fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# Looping through string
for x in "banana":
    print(x)

# Using the break statement
for x in fruits:
    print(x)
    if x == "banana":
        break

# Using the continue statement
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Else in for loop
for x in range(6):
    print(x)
else:
    print("finally finished")

# Nested for loop
adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x, y)
