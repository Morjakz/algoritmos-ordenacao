import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

lista = []

for i in range(100000):
    d100000 = random.randint(0, 10000)
    lista.append(d100000)
print(f'A lista é: {lista}')
print(f'\nNúmero de elementos da lista: {(len(lista))} elementos')

resultado = insertion_sort(lista)
print(f'A lista ordenada é: {resultado}')

# Estável
# O(n), O(n* n), O(n* n) para o melhor, médio e pior caso, respectivamente.
# Melhor caso: o array já está ordenado
# Caso médio: o array está ordenado aleatoriamente
# Pior caso: o array está ordenado em ordem inversa.