def mergeSort(arr):
    newArr = []
    mid = len(arr) // 2
    
    if(len(arr) <= 1):
        return arr
    
    listEsq = arr[:mid]
    listDir = arr[mid:]
    
    listEsq = mergeSort(listEsq)
    listDir = mergeSort(listDir)
    
    while listEsq and listDir:
        if(listEsq[0] > listDir[0]):
            newArr.append(listDir[0])
            listDir.pop(0)
        else:
            newArr.append(listEsq[0])
            listEsq.pop(0)
    
    newArr.extend(listEsq)
    newArr.extend(listDir)
    
    return newArr
