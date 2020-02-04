def operation(fonct, x, y):
    return fonct(x,y)

x = int(input("valeur de x : "))
y = int(input("valeur de y : "))
choix_operation = input("Operation a realiser sur x et y : addition (a) ou multiplication (m) ? : ")

if choix_operation == "a":
    print("le resultat est : ", operation((lambda x, y : x + y), x, y))
elif choix_operation == "m":
    print("le resultat est : ", operation((lambda x, y : x * y), x, y))
else:
    print("choix non pris en compte")
