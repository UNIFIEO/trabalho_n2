import random
import time

# Função para gerar uma lista de números aleatórios
def gerar_lista(tamanho, limite=1000):
    return [random.randint(1, limite) for _ in range(tamanho)]

# Algoritmos de ordenação
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

# Algoritmos de busca
def busca_linear(arr, alvo):
    for i in range(len(arr)):
        if arr[i] == alvo:
            return i
    return -1

def busca_binaria(arr, alvo):
    inicio, fim = 0, len(arr) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# Função para medir tempo de execução
def medir_tempo(algoritmo, arr):
    inicio = time.time()
    algoritmo(arr)
    return time.time() - inicio

# Função principal para testes
def main():
    tamanho = 1000  # Define o tamanho da lista
    lista_original = gerar_lista(tamanho)

    # Testando métodos de ordenação
    for algoritmo in [bubble_sort, selection_sort, insertion_sort]:
        lista = lista_original.copy()
        tempo = medir_tempo(algoritmo, lista)
        print(f"{algoritmo.__name__}: {tempo:.5f} segundos")

    # Preparando a lista ordenada para busca binária
    lista_ordenada = sorted(lista_original)

    # Testando métodos de busca
    alvo = random.choice(lista_original)
    for algoritmo in [busca_linear, busca_binaria]:
        inicio = time.time()
        resultado = algoritmo(lista_ordenada if algoritmo == busca_binaria else lista_original, alvo)
        tempo = time.time() - inicio
        print(f"{algoritmo.__name__} encontrou {alvo} na posição {resultado} em {tempo:.5f} segundos")

if __name__ == "__main__":
    main()
