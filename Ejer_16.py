"""Utilice cola de prioridad (Heap utilizo), para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión."""

from heap import HeapMax


h = HeapMax()

print()
print("a) cargue tres documentos de empleados")
h.agregar(['documento_emple_1', None], 1)
h.agregar(['documento_emple_2', None], 1)
h.agregar(['documento_emple_3', None], 1)
print(h.vector)
print()
print("b) imprima el primer documento de la cola (y eliminar)")
print(h.quitar()[0][0])

print()
print("c) cargue dos documentos del staff de TI")
h.agregar(['documento_staff_1', None], 2)
h.agregar(['documento_staff_2', None], 2)
print(h.vector)
print()

print("d) cargue un documento del gerente")
h.agregar(['documento_gerente_1', None], 3)
print(h.vector)
print()

print("e) imprima los dos primeros documentos de la cola.")
print(h.quitar()[0][0])
print(h.quitar()[0][0])
print()
print(h.vector)
print()
print('f) cargue dos documentos de empleados y uno de gerente.')
h.agregar(['documento_emple_4', None], 1)
h.agregar(['documento_emple_5', None], 1)
h.agregar(['documento_gerente_2', None], 3)
print()

print('g) imprima todos los documentos de la cola de impresión')
for i in range(h.tamanio):
    print(h.quitar()[0][0])

print(h.vector)

