'''
Binary search algorithm to find index of a key in an array
O(logn), each iteration of loop reduces options in half
'''
def binary_search(key, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = low + (high - low) // 2
        if arr[middle] == key:
            return middle
        if arr[middle] < key:
            low = middle + 1
        elif arr[middle] > key:
            high = middle - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(9, arr))