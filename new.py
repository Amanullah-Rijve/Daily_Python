import re

text = "Hello I am Learning Python"
text = "#% * &() T ^ & Hello iwegckljfdv"

print(re.search(" & ", text))

print(re.findall("[e-o]",text))

money =  " That Will Be 69 taka only"

print(re.findall("\d",money))

name = " Hi Mexico"

print(re.findall("Me...o",name))


name = " Hi Mexico"

print(re.findall("Me.*o",name))




