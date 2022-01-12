# the try block will generate an error, because x is not defined

try:
    print(x)
except:
    print("An exception occured")


# the try block will generate a NameError, because x is not defined

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


# the try block does nto raise any errors, so the else block is executed

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


# the finally block gets executed no matter if the try block raises any errors or not:

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
