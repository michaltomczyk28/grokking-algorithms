def recursive_sum(arr):
    if arr == []:
        return 0
    
    return arr[0] + recursive_sum(arr[1:])

print(recursive_sum([1, 2, 3, 4, 5]))