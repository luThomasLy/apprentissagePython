def division(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as err:
        print("La divsion par zero n'est pas admise")

# def eval():
#     a=3
#     b=0
#     if b==0:
#         raise Exception("division par zero")
#     print(a/b)

def main():
    division(12, 0)
    # eval()

main()