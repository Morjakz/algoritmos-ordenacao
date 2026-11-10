import random 

def selection_sort(arr):
    if not arr:
        return arr
    for i in range(len(arr)):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

lista = []

for i in range(100000):
    d100000 = random.randint(0, 10000)
    lista.append(d100000)
print(f'A lista é: {lista}')
print(f'\nNúmero de elementos da lista: {(len(lista))} elementos')

resultado = selection_sort(lista)
print(f'A lista ordenada é: {resultado}')