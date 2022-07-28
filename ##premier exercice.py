##premier exercice
animaux=  ['chat', 'chien','oiseau']

class Animal :
    def __init__(self, type) :
        self.type= type

    def moyen_de_déplacement (self) :
        if self.type in ('chien','chat'):
            self.mdp= 'marche'
           
        elif self.type == 'poisson':
            self.mdp= 'nage'
           
        elif self.type == 'oiseau' :
            self.mdp= 'vole'
           
        else :
            raise ValueError("animal non pris en compte")

        print(f" {self.type} {self.mdp} ")



    def lieu_d_habitat (self) :
        if self.type in ('chien','chat','oiseau') : 
            self.lieu= 'terre'

        elif self.type == 'poisson' :
            self.lieu = 'mer'

        else :
            raise ValueError("non pris en compte")

        print(f" {self.type} {self.lieu} ")


an=Animal('hj')
an.moyen_de_déplacement()
an.lieu_d_habitat()

