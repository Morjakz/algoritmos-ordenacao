import random

def radix_sort(arr):
    max_num = max(arr)
    exp = 1  # Representa a posição atual do dígito (1, 10, 100, ...)

    while max_num // exp > 0:
        n = len(arr)
        output = [0] * n
        count = [0] * 10  # Para digitos de 0-9

        # Contagem de ocorr~encias de cada dígito 
        for num in arr:
            index = (num // exp) % 10
            count[index] += 1

        # Converte o count[] para posições reais
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Constrói a aída da lista(em reverso para estabilidade) 
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        # Copia a sapida para a lista[]
        for i in range(n):
            arr[i] = output[i]

        exp *= 10
    return arr

lista = []

for i in range(100000):
    d100000 = random.randint(0, 10000)
    lista.append(d100000)
print(f'A lista é: {lista}')
print(f'\nNúmero de elementos da lista: {(len(lista))} elementos')

resultado = radix_sort(lista)
print(f'A lista ordenada é: {resultado}')