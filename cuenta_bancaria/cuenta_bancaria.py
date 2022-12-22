class Padre:
    def hablar(self):
        print("hola")


class Madre:
    def reir(self):
        print("ja ja ja")

    def hablar(self):
        print("que tal")


class Hijo(Padre, Madre): # Podemos heredar multiples clases, siempre respeta el orden en que se colocan
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

mi_nieto.reir()
mi_nieto.hablar()