from cola import Cola

class Personaje:
    def __init__(self, n_personaje=None, n_superheroe=None, g=None):
        self.nombre_personaje = n_personaje
        self.nombre_superheroe = n_superheroe
        self.genero = g

    def __str__(self):
        return f"{self.nombre_personaje}, {self.nombre_superheroe}, {self.genero}"

#mostrar cola
def mostrar_cola(cola):
    for i in range(0,cola.tamanio()):
        print(cola.mover_al_final())

#funcion para encontrar un personaje por su nombre de superheroe
def buscar_por_nombre_de_superheroe(cola, buscado):
    for i in range(0,cola.tamanio()):
        superheroe=cola.mover_al_final()
        if superheroe.nombre_superheroe == buscado:
            return superheroe

#funcion para mostrar un superheroe por su genero
def mostrar_personaje_de_x_genero(cola, g):
    for i in range(0,cola.tamanio()):
        superheroe=cola.mover_al_final()
        if superheroe.genero == g:
            print(superheroe)

#funcion para encontrar un personaje por su nombre de personaje
def buscar_por_nombre_personaje(cola, buscado):
    for i in range(0,cola.tamanio()):
        superheroe=cola.mover_al_final()
        if superheroe.nombre_personaje == buscado:
            return superheroe

#funcion para encontrar un nombre de personaje o nombre de superheroe por la letra inicial
def mostrar_por_letra(cola, buscado):
    for i in range(0,cola.tamanio()):
        personaje=cola.mover_al_final()
        #if personaje.nombre_personaje[0] or personaje.nombre_superheroe[0]== buscado:
        if buscado in (personaje.nombre_personaje[0], personaje.nombre_superheroe[0]):
            print(personaje)



cola_de_personajes=Cola()
cola_de_personajes.arribo(Personaje('Tony Stark','Iron Man', 'M'))
cola_de_personajes.arribo(Personaje('Steve Rogers', 'Capitán América', 'M'))
cola_de_personajes.arribo(Personaje('Natasha Romanoff','Black Widow', 'F'))
cola_de_personajes.arribo(Personaje('Carol Danvers', 'Capitana Marvel', 'F'))
cola_de_personajes.arribo(Personaje('Carlos', 'shrek', 'M'))
cola_de_personajes.arribo(Personaje('Scott Lang', 'Ant-Man', 'M'))

mostrar_cola(cola_de_personajes)
print()
print('a')
print(buscar_por_nombre_de_superheroe(cola_de_personajes,'Capitana Marvel'))
print()
print('b')
print('TODOS LOS FEMENINOS')
mostrar_personaje_de_x_genero(cola_de_personajes,'F')
print()
print('c')
print('TODOS LOS MASCULINOS')
mostrar_personaje_de_x_genero(cola_de_personajes,'M')
print()
print('d')
print(buscar_por_nombre_personaje(cola_de_personajes,'Scott Lang'))
print()
print('e')
mostrar_por_letra(cola_de_personajes,'S')
print()
print('f')
personaje_buscado= buscar_por_nombre_personaje(cola_de_personajes,'Carol Danvers')
if personaje_buscado!=None:
    print(personaje_buscado)
else:
    print('no se encuentra en la cola')