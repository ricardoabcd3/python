import random
from typing import cast
def busqueda_lineal(lista, objetivo):
    match = False
    global c
    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            c=lista.count(elemento)
            break
            

    return match 


if __name__ == '__main__':
    c=0
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    lista=sorted(lista)

    encontrado = busqueda_lineal(lista, objetivo)
    
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print("numero de veces repetido: ",c)
    print(lista)