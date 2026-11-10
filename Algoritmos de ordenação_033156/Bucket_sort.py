import random

def bucketSort(list):
    bucket = []

    # Cria buckets (baldes) vazios
    for i in range(len(list)):
        bucket.append([])

    # Insere os elementos em seus respectivos buckets 
    for j in list:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Ordena os elementos de cada bucket 
    for i in range(len(list)):
        bucket[i] = sorted(bucket[i])

    # Pega o elemento ordenado 
    k = 0
    for i in range(len(list)):
        for j in range(len(bucket[i])):
            list[k] = bucket[i][j]
            k += 1
    return list

lista = []

for i in range(100000):
    d100000 = random.uniform(0, 10000)
    lista.append(d100000)
print(f'A lista é: {lista}')
print(f'\nNúmero de elementos da lista: {(len(lista))} elementos')

resultado = bucketSort(lista)
print(f'\nA lista ordenada é: {resultado}')

# Complexidade Temporal	 
# Melhores	O(n+k); Pior O(n2); Média O(n)
# Estável 
# A ordenação por balde é usada quando: a entrada é distribuída uniformemente em uma faixa
# e existem valores de ponto flutuante