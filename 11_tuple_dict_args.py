def multi_args_tuple(*args):
    for n in args:
        print("arg :", n)

#multi_args_tuple(3)
#tuple étendu
multi_args_tuple(2,3,4,5)


def multi_args_dict(**kwargs):
    for m in kwargs.keys():
        print(m, "correspond à kwarg :", kwargs.get(m))

#dictionnaire étendu
my_dict = {'1':"lundi",'2':"mardi"}
multi_args_dict(**my_dict)