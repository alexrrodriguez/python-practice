import datetime

# create datetime variable

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

# create date

x = datetime.datetime(2023, 5, 17)
print(x)
print(x.strftime("%B"))
