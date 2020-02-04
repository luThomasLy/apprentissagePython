class Personne():
    def __init__(self, nom, age = 0, taille = 55):
        self.nom = nom
        self.age = age
        self.taille = taille
    def __lt__(self, other):
        return self.age < other.age
        #return "Comparaison basée sur l'âge : {} est plus > que {}".format(self.age < other.age)
    def __lt__(self, other):
        return self.taille < other.taille

Al = Personne("Alice",4,106)
Bo = Personne("Bob",5,105)
print(Al < Bo)

