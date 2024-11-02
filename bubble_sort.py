def bubble_sort(arr):
    # O(n^2) due to nested loop
    for i in range(len(arr) - 1, 0, - 1):
        for j in range(i):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


arr1 = [5, 3, 8, 6, 7, 2]
bubble_sort(arr1)
print(arr1)