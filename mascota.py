class Mascota:
    # matodo constructor
    def __init__(self, nombre, raza):
        self.nombre=nombre
        self.raza=raza

# Metodos Getter y Setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        if len(nombre)>0:
            self.nombre=nombre
        else:
            print("EL nombre no puede estar vacia")

    def get_raza(self):
        return self.raza

    def set_raza(self,raza):
        if len(raza)>0:
            self.raza=raza
        else:
            print("La raza no puede estar vacia")

    #imprimir la informacion de la clase

    def __str__(self):
        return f'Nombre:{self.nombre}, Raza: {self.raza}'