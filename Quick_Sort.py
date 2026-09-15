def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


arr = [5, 2, 8, 1, 9, 3, 5]

print(quick_sort(arr))