notes1 = [12,10,4]
#notes.insert(1,99) à l'index 1, on ajoute 99
notes1.insert(1,99)
#supprime la valeur à l'index 0
notes1.pop(0)
#inverse les valeurs
notes1.reverse()
print(notes1)

notes2 = [0,1,2,3,4,5,6,7,8,9]
print(notes2[5::2])

print(notes2[len(notes2)-1])
print(notes2[-1])
#entre 0 et 5, tous les 2 chiffres 0 à 2 à 4
print(notes2[0:5:2])
print(max(notes2))

# jours_semaine = ["lundi","mardi","mercredi","jeudi","vendredi"]
# jours_week = ["samedi","dimanche"]
# #rajoute les jours_week à jours_semaine
# jours_semaine.extend(jours_week)
# print(jours_semaine)
# print(jours_semaine[-1])
# print(jours_semaine[-3])