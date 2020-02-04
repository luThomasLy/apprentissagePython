# n = int(input("n ? "))
# c = int(input("c ? "))

def fonction_damier(n,c):
    nb_lignes = n * c
    damier = ""
    while nb_lignes > 0 : # lignes
        nb_lignes = nb_lignes - 1
        ligne = ""
        nb_col = n * c
        while nb_col > 0 : # colonnes
            nb_col = nb_col - 1
            a = nb_lignes // c
            b = nb_col // c
            if (a+b)%2 == 0:
                ligne = ligne + "."
            else:
                ligne = ligne + "#"
        #print(ligne)
        damier = damier + ligne + "\n"
    return damier

my_damier = fonction_damier(3,4)
print(my_damier)

# a = int(input("a ? "))
# b = int(input("b ? "))
# fonction_damier(a,b)