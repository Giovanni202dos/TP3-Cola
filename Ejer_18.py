from cola import Cola

from random import randint

#mostrar cola
def mostrar_cola(cola):
    for i in range(0,cola.tamanio()):
        print(cola.mover_al_final())

def letra_con_mas_turno(cola):
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    for i in range(0,cola.tamanio()):
        dato=cola.mover_al_final()
        if dato[0]=='A':
            a+=1
        elif dato[0]=='B':
            b+=1
        elif dato[0]=='C':
            c+=1
        elif dato[0]=='D':
            d+=1
        elif dato[0]=='E':
            e+=1
        elif dato[0]=='F':
            f+=1
    vec=[]
    if a==max(a,b,c,d,e,f):
        vec.append('a')
    if b==max(a,b,c,d,e,f):
        vec.append('b')
    if c==max(a,b,c,d,e,f):
        vec.append('c')
    if d==max(a,b,c,d,e,f):
        vec.append('d')
    if e==max(a,b,c,d,e,f):
        vec.append('e')
    if f==max(a,b,c,d,e,f):
        vec.append('f')
    if max(a,b,c,d,e,f)>0:
        return vec, max(a,b,c,d,e,f)
    else:
        return None, 0



        



cola_de_turnos=Cola()
for i in range(10):
    letra=(chr(randint(65, 70)))
    codigo=letra+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    cola_de_turnos.arribo(codigo)
print()

cola_1=Cola()
cola_2=Cola()

for i in range(0,cola_de_turnos.tamanio()):
    codigo=cola_de_turnos.atencion()
    if codigo[0] in ('A','C','F'):
        cola_1.arribo(codigo)
    else:
        cola_2.arribo(codigo)

print('cola_1')
mostrar_cola(cola_1)
print()
print('cola_2')
mostrar_cola(cola_2)
if cola_1.tamanio()>cola_2.tamanio():
    print('cola_1 tiene mas turnos')
    v=letra_con_mas_turno(cola_1)
    print('en cola_1 la letra de mayor turnos es:',v[0],'y su cantidad es:',v[1])

else:
    print('cola_2 tiene mas turnos')
    v=letra_con_mas_turno(cola_2)
    print('en cola_2 la letra de mayor turnos es:',v[0],'y su cantidad es:',v[1])



def turnos_mayores_a_506(cola):
    print('los numeros mayores a 506 son: ')
    for i in range(0,cola.tamanio()):
        dato=cola.mover_al_final()
        if int(dato[1:])>506:
            print(dato)

if cola_1.tamanio()<cola_2.tamanio():
    print('cola_1 tiene menos turnos')
    turnos_mayores_a_506(cola_1) 
else:
    print('cola_2 tiene menos turnos')
    turnos_mayores_a_506(cola_2)




