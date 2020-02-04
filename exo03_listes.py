liste_courses=["carrotes","ananas","tomates","courgettes"]
print("{}, {}, {}, {}".format(liste_courses[0], liste_courses[1], liste_courses[2], liste_courses[3]))

liste_courses.append("riz")
liste_courses.sort()
print("Liste des courses : ", liste_courses)

liste_courses.pop(2)
print("Liste des courses : ", liste_courses)
