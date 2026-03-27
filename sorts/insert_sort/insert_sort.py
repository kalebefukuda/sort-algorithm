def insertSort(arr):
    comparacoes = 0
    trocas = 0

    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if arr[j] > current_value:
                arr[j + 1] = arr[j]
                trocas += 1
                j -= 1
            else:
                break
        arr[j + 1] = current_value

    return arr, comparacoes, trocas