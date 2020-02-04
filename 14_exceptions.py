# def division(a,b):
#     if b==0:
#         raise Exception("division par zero")
#     print(a/b)

def division(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as err:
        print(err)


print("debut du prog")
division(3,0)

# try:
#     import mathh
#     division(3,0)
# except ZeroDivisionError as err:
#     print("erreur ! div par zero", err)
# except ModuleNotFoundError as err:
#     print(err)
#     print("erreur ! module not found")
#     exit()

print("fin du prog")