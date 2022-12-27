import math

def recursive_max(arr):
    if len(arr) == 0:
        return -math.inf
    
    current_max = recursive_max(arr[1:])
    
    return arr[0] if arr[0] > current_max else current_max


print(recursive_max([-42, 15, 2, 156, 12, 512, 6]))