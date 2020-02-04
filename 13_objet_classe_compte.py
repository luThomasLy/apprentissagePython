class Compte():
    # def __init__(self):
    #     self.solde = 0
    #     self.num = 0
    def __init__(self, _solde = 0, _num = 0):
        self._solde =_solde
        self._num =_num
    # def __init__(self, solde, num):
    #     self.solde = solde
    #     self.num = num
#principe d'encapsulation
    #get
    @property
    def solde(self):
        print(" je suis le getter ")
        return self._solde
    #set
    @solde.setter
    def solde(self, nouveau_solde):
        print(" je suis le setter ")
        self._solde = nouveau_solde

    def __str__(self):
        return super().__str__()+"Le solde du compte n° : {} est de {:.2f} ".format(self._num, self._solde)

    def __gt__(self, other):
        return self.solde > other.solde

    def __eq__(self, o: object) -> bool:
        return self._num == o._num

    def __repr__(self) -> str:
        return "({},{})".format(self._num,self._solde)


#c_1 = Compte()
c_1 = Compte(10,2)
c_2 = Compte(30,2)
#print(c_1)
print(c_1)
liste = [c_1,c_2]
print(liste)

# print(c_1>c_2)
# print(c_2.solde)
# c_2.solde = 5