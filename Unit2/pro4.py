def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


arr = [64, 34, 25, 12, 23, 54, 45]
arr2 = []
print("Unsorted array is :")
print(arr)
bubbleSort(arr)
print("Sorted array is :")
for i in arr:
    arr2.append(i)
print(arr)