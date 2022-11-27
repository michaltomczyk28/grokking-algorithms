def  find_min(arr):
    min_index = 0;
    for i in range(len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    
    return min_index

# O(n^2)
def selection_sort(arr):
    result = []
    while len(arr) > 0:
        min = find_min(arr)
        result.append(arr.pop(min))
    
    return result

print(selection_sort([32, 13, 52, 51, 3, -3, -2, 15, 2]))