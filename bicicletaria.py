class Bicicleta:
    def __init__(self, marca, cor, marchas, usada=True):
        self.marca = marca
        self.cor = cor
        self.marchas = marchas
        self.usada = usada

    def buzinar(self):
        print('priiiiimmmmmmm')

    def brecar(self):
        print("Brecando .....")
        print("Parado.....")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b = Bicicleta("Caloi", 'Laranja', 10)
print(b)

b.buzinar()
b.brecar()
