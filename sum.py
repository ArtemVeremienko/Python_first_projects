def sum(arr):
    if arr == []:
        return 0
    return 1 + sum(arr[1:])

print ( sum([1,2,3,4]) )
