# create class
class MyClass:
    x = 5


# create object
p1 = MyClass()
print(p1.x)


# init function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create object
    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

p1.myfunc()


# self parameter variable names can be changed

class Person:
    def __init__(sillyobject, name, age):
        sillyobject.name = name
        sillyobject.age = age

    # create object
    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)

p1.myfunc()

# modify objects
p1.age = 40

print(p1.age)

# delete object properties
del p1.age


print(p1.age)

# delete an object
del p1

print(p1)
