import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

# this pip method capitalizes the first letter of each word

print(c.hump(txt))
