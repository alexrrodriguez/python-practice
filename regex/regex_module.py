import re

txt = "The rain in Spain"

# Check  if the string starts with "The" and ends with "Spain"

x = re.search("^The.*Spain$", txt)

if x:
    print("Yes! There is a match.")
else:
    print("No matches")

# using findall function to return a list containing every occurrence of "ai"

x = re.findall("ai", txt)

print(x)

# use the search function to show the position of the first white space character

x = re.search("\s", txt)

print("The first white space character is located in position:", x.start())

# use the split function to split the string at every white space character

x = re.split("\s", txt)

print(x)

# use the sub function to replace all white space characters with the digit "9"

x = re.sub("\s", "9", txt)

print(x)
