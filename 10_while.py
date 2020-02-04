ma_liste = [5,3,9,4]
#ma_liste = [5,3,8,4]
i = 0

condition = True
while condition and i < len(ma_liste) :
    if ma_liste[i] == 9 :
        condition = False
        print(ma_liste[i], " bingo ! indice : ", i)
    i += 1
if condition == True:
    print("nothing")