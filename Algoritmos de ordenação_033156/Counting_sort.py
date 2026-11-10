import random

def counting_sort(arr):
    # Encontrar o valor máximo na lista
    max_val = max(arr)
    min_val = min(arr)

    # Tamanho do intervalo de valores
    range_of_elements = max_val - min_val + 1

    # Criando um array de contagem com base no intervalo
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Contar a ocorrência de cada valor
    for num in arr:
        count[num - min_val] += 1

    # Alterar o array de contagem para armazenar a posição correta de cada número
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Construir o array ordenado
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

lista = []

for i in range(100000):
    d100000 = random.randint(0, 10000)
    lista.append(d100000)
print(f'A lista é: {lista}')
print(f'\nNúmero de elementos da lista: {(len(lista))} elementos')

resultado = counting_sort(lista)
print(f'Lista ordenada: {resultado}')