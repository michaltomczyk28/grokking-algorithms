def recursive_count(arr):
    if arr == []:
        return 0
    
    return 1 + recursive_count(arr[1:])

print(recursive_count([1, 2, 3]))