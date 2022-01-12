# read whole file
f = open("demofile.txt", "r")

print(f.read())

# read part of file
f = open("demofile.txt", "r")

print(f.read(5))

# read a line of a file
f = open("demofile.txt", "r")

print(f.readline())

# loop through lines to read whole file
f = open("demofile.txt", "r")
for x in f:
    print(x)
