import random

def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    # Se o maior não é a raiz, troca e continua descendo
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)


def heap_sort(arr):
    n = len(arr)

    # Fase 1: construir o max-heap
    # (começa no último nó que tem filhos e vai até a raiz)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Fase 2: extrair o maior elemento um a um
    for fim in range(n - 1, 0, -1):
        arr[0], arr[fim] = arr[fim], arr[0]  # move o maior para o final
        heapify(arr, fim, 0)                 # reconstrói o heap reduzido

    return arr

lista = []

for i in range(100000):
    d100000 = random.randint(0, 10000)
    lista.append(d100000)
print(f'A lista é: {lista}')
print(f'\nNúmero de elementos da lista: {(len(lista))} elementos')

resultado = heap_sort(lista)
print(f'Lista ordenada: {resultado}')