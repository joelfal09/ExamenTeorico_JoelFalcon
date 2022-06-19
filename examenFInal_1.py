import random

listaNum = []


def num_aleatorio():
    for i in range(1, 11):
        listaNum.append(random.randint(1, 30))

    return listaNum


def numeros_no_repetidos(listaNum):
    lista_sin_repetidos = []
    for i in listaNum:
        if not i in lista_sin_repetidos:
            lista_sin_repetidos.append(i)
    return lista_sin_repetidos


listaNum = num_aleatorio()
print(listaNum)
lista_sin_repetidos = numeros_no_repetidos(listaNum)
print(lista_sin_repetidos)

lista_ordenada_descendente = sorted(lista_sin_repetidos, reverse=True)
print(lista_ordenada_descendente)

lista_ordenada_ascendente = sorted(lista_sin_repetidos, reverse=False)
print(lista_ordenada_ascendente)


def mayor_lista(lista):
    max_lista = max(lista)
    return max_lista


print(f'El mayor valor de la lista es: {mayor_lista(lista_sin_repetidos)}')
