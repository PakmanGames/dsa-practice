def selection_sort(arr):
    # O(n^2) due to nested loops
    for i in range(len(arr) - 1): # 1 assignment, n iterations, n - 1 comparisons
        idx_current_min = i # n iterations * (1 assignment)
        for j in range(i + 1, len(arr)): # n iterations * (1 assignment, n iterations, n - 1 comparisons)
            if (arr[j] < arr[idx_current_min]): # n iterations * n iterations * (1 comparison)
                idx_current_min = j # n iterations * n iterations * (1 assignment)
        arr[i], arr[idx_current_min] = arr[idx_current_min], arr[i] # n iterations * (2 assignments)

arr = [5, 3, 8, 6, 7, 2, 1, 4]
selection_sort(arr)
print(arr)