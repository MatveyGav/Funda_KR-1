def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    pivot = arr[mid]
    left = [x for x in arr[:mid] + arr[mid + 1:] if x < pivot]
    right = [x for x in arr[:mid] + arr[mid + 1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
