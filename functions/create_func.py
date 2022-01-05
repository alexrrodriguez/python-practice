def my_function():
    print("Hello from a function")


my_function()


# adding parameters


def my_function(fname):
    print(fname + " Torvald")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


# default parameters


def my_country(country="Norway"):
    print("I am from " + country)


my_country("Sweden")
my_country("India")
my_country()
my_country("Brazil")
