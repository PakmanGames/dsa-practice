# Compares elements to the left, shifts over to the right to make room to insert a new value
def insertion_sort(arr):
    # O(n^2) due to nested loops
    # Best case of O(n) (selection was O(n^2))
    for i in range(1, len(arr)):
        temp = arr[i]
        left_idx = i - 1
        while left_idx >= 0 and arr[left_idx] > temp:
            arr[left_idx + 1] = arr[left_idx]
            left_idx -= 1
        arr[left_idx + 1] = temp

arr = [5, 3, 8, 6, 7, 2, 1, 4]
insertion_sort(arr)
print(arr)