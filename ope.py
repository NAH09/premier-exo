nombre= []

class Addition : 
    def __init__(self, nombre) :
        self.nombre= nombre

    def check (self) :
        self.vald=True
        print ('validé')
        for s in self.nombre :
            if not isinstance(s, (int)) :
                self.vald =False
                raise ValueError('entrez un entier')

    def product (self):
        self.prod=1
        for s in self.nombre:
            self.prod *= s
        return self.prod

ir= Addition([8,8,8])
ir.check()
ir.product()