import re

#test1
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")

#test2
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)

#test3
chat_regex = re.compile('^chat')
print(chat_regex)

c = chat_regex.search("un chat")
print(c)

d = chat_regex.search("chaton")
print(d)

e = type(chat_regex)
print(e)