import random

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivô = array[-1]  # Escolhe o último elemento como pivô
    menores = [x for x in array[:-1] if x <= pivô]
    maiores = [x for x in array[:-1] if x > pivô]

    return quick_sort(menores) + [pivô] + quick_sort(maiores)

lista = []

for i in range(100000):
    d100000 = random.randint(0, 10000)
    lista.append(d100000)
print(f'A lista é: {lista}')
print(f'\nNúmero de elementos da lista: {(len(lista))} elementos')

resultado = quick_sort(lista)
print(f'A lista ordenada é: {resultado}')