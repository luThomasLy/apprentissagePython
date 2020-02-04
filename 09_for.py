#for 1
formations = ["C","C++","Python"]
for fm in formations :
    print(fm,len(fm))

#for 2
ma_liste1 = [5,3,9,4]
indice = 0
for elt in ma_liste1 :
    if elt == 9 :
        #break = il va s'arreter au 9
        #continue = il va aller à la fin du tableau
        print(elt, "bingo ! indice : ", indice)
    indice = indice + 1
    # alternative : i += 1 / faux : i++

#for 3 avec range = fonction génératrice
ma_liste2 = [6,4,10,5]
for indice in range(0,len(ma_liste2)) :
    print("range :", ma_liste2[indice])

#remplissage et initialisation de tableau avec un for
my_list=[]
for i in range(20):
    #nb pair if i%2 == 0 :
    my_list.append(i)
print(my_list)

my_list2=[2*i for i in range(20) if i%2 == 0]
print(my_list2)

#for dans les tableau
a = [1,2,3,4,5,6,7]
carres = [nb*nb for nb in a]
print(carres)

carres_pairs = [nb*nb for nb in a if nb%2==0]
print(carres_pairs)