def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Example
arr = [64, 34, 25, 12, 22, 11, 90]

print("Sorted array:", bubble_sort(arr))