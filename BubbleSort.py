def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            print(f"Stopping early at pass {i + 1}")
            break
    return arr

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort_optimized(unsorted_list))
already_sorted = [1, 2, 3, 4, 5]
print("Sorted array:", bubble_sort_optimized(already_sorted))