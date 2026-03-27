def mergeSort(arr, _comparacoes=None, _trocas=None):
    if _comparacoes is None:
        _comparacoes = [0]
        _trocas = [0]

    if len(arr) <= 1:
        return arr, _comparacoes[0], _trocas[0]

    mid = len(arr) // 2
    listEsq, _, _ = mergeSort(arr[:mid], _comparacoes, _trocas)
    listDir, _, _ = mergeSort(arr[mid:], _comparacoes, _trocas)

    newArr = []
    while listEsq and listDir:
        _comparacoes[0] += 1
        if listEsq[0] > listDir[0]:
            newArr.append(listDir[0])
            listDir.pop(0)
        else:
            newArr.append(listEsq[0])
            listEsq.pop(0)
        _trocas[0] += 1

    newArr.extend(listEsq)
    newArr.extend(listDir)

    return newArr, _comparacoes[0], _trocas[0]