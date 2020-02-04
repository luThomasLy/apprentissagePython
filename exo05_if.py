import math

# nb_entier = int(input("saisir un entier : "))
#
# if nb_entier < 0 :
#     print("erreur :", nb_entier)
# else:
#     print("la racine :", math.sqrt(nb_entier))
#     print("la racine :", abs(nb_entier))

nb_absolue = int(input("saisir un nb_absolue : "))

if nb_absolue < 0 :
    #mise en positif avec le -nb_absolue
    #fonction abs() egalement
    nb_absolue = -nb_absolue
    print("la valeur absolue :", nb_absolue)