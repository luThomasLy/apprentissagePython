class Rectangle():
    def __init__(self, _longueur, _largeur, _nom = "rectangle"):
        self._nom =_nom
        self._longueur =_longueur
        self._largeur =_largeur

    def __str__(self) -> str:
        return "({},{})".format(self._nom, self._largeur,self._longueur)

    @property
    def nom(self):
        return self._nom

    @property
    def longueur(self):
        return self._longueur

    @property
    def largeur(self):
        return self._largeur

    @nom.setter
    def nom(self, nom):
        self._nom=nom

    @largeur.setter
    def largeur(self, largeur):
        self._largeur=largeur

    @longueur.setter
    def longueur(self, longeur):
        self._longueur=longeur

rectangle = Rectangle(3,2)

def affichage_rect():
    return print(rectangle)

#correction doublon avec perimetre_carre
def perimetre_rect():
    return print(rectangle._nom, rectangle._largeur*rectangle._longueur)

#rectangle.largeur=1
affichage_rect()
perimetre_rect()

class Carre(Rectangle):
    def __init__(self, _longueur, _largeur, _nom):
        super().__init__(_longueur, _largeur, _nom)

def affichage_carre():
    return print(carre)

carre = Carre(10,10,"carre")

def perimetre_carre():
    return print(carre._nom, carre._largeur*carre._longueur)

affichage_carre()
perimetre_carre()
