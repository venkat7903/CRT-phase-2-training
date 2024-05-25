def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [100,100,  99, 1, 500, 29]
print(selectionSort(arr))