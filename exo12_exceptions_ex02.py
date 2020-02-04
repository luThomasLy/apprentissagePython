import time

def verif_div():
    while True:
        tps = time.strftime("%H:%M:%S")
        try:
            x = int(input("saisir x : "))
            y = int(input("saisir y : "))
            print(x/y)
            print(tps)
            break
        except ValueError:
            print("la valeur n'est pas correcte")
            print(tps)
        except ZeroDivisionError:
            print("La divsion par zero n'est pas admise")
            print(tps)
    print("Au revoir !")

def main():
    verif_div()

main()