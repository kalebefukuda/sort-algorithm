def bubbleSort(arr):
    if len(arr) <= 1:
        return arr, 0, 0

    comparacoes = 0
    trocas = 0

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1

    return arr, comparacoes, trocas