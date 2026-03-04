from mascota import Mascota
# imprimir la informacion de la clase 
mascota=Mascota('firulais', 'Pastor Aleman')
print(mascota.get_nombre())
mascota.set_nombre("Tommy")
mascota.set_raza(" Husky Siberiano")
print(mascota.get_nombre())
print(mascota)