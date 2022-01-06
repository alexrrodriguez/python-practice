# use a module

import platform
import mymodule as mx
import mymodule
# import object from module
from mymodule import person1

mymodule.greeting("Johnathan")

# using variables in module

a = mymodule.person1["age"]
print(a)

# renaming a module

a = mx.person1["age"]
print(a)

# built in modules

x = platform.system()
y = platform.processor()
print(x)
print(y)

# using dir() function

a = dir(platform)
print(a)

# import from module

print(person1["age"])
