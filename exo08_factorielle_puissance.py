import time

#recursive : s'appelle elle même
def factorielle_int(n):
    if n<2:
        return 1
    else:
        return n*factorielle_int(n-1)
print(factorielle_int(3))

start_time = time.time()
print("--- %s seconds recursive ---" % (time.time() - start_time))

#iterative
def puissance_int(x,y):
    result = 1
    compteur = 0
    while y > 0:
        if y % 2 != 0:  # y impair
            result *= x
        x *= x
        y //= 2  # division entière par 2
        compteur = compteur + 1
        print("compteur :", compteur)
    return result
print("puissance n d'un entier :", puissance_int(2,2))