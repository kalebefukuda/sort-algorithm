arr = [5,4,3,2,1]

def bubbleSort(arr):
    if (len(arr) <= 1):
        return arr
    aux = 0
    for i in range(0,len(arr)):
        for j in range(0,len(arr) - i - 1):
            if (arr[j] > arr[j + 1]):
                aux = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = aux
    return arr

print(buble(arr))
