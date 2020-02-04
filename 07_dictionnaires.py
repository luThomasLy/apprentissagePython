my_dict={0:"lundi", 1:"mardi", 2:"mercredi", 3:"jeudi", 4:"vendredi", 5:"samedi", 6:"dimanche"}
#print(my_dict[0])

for key,value in my_dict.items():
    print(key,value)

for x in my_dict:
    print(x)

for x in my_dict:
    print(my_dict[x])

if 3 in my_dict:
    print("yes")
else:
    print("no")