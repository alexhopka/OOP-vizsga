from abc import ABC, abstractmethod
class Utanfuto(ABC):
    @abstractmethod
    def attributumok(self):
        pass
class Tipusok:
    def __init__(self, tipus, teherbiras):
        self.tipus = tipus
        self.teherbiras = teherbiras

    def printname(self):
        print(self.tipus, self.teherbiras)
class Utanfuto(Tipusok):
    def __init__(self, tipus, teherbiras, ev):
        super().__init__(tipus, teherbiras)
        self.kolcsonzes = 2024
    def kolcsonzott(self):
        print("A jármű",self.tipus,self.teherbiras,"teherbírású, és",self.kolcsonzes,"-ben kölcsönözték ki")

x = Utanfuto("ponyvázott","250kg",2024)
x.kolcsonzott()