def findSmallest(arr):
    smallest = arr[0]
    smallest_index= 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

arr = [23, 2, 3, 11, 7, 6, 5]
print( selectionSort(arr) )
