# O(log n)
def binary_search(arr, value):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if value == arr[mid]:
            return mid
        elif value > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return None


arr = [1, 3, 4, 7, 9, 10, 14, 15, 19, 25, 32, 53]
print(binary_search(arr, 53))