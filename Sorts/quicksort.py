def partition(arr, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if arr[i] <= arr[begin]:
            arr[i], arr[pivot] = arr[pivot], arr[i]  # perform swap
        arr[pivot], arr[begin] = arr[begin], arr[pivot]  # perform last swap

    return pivot


def quickSort(arr, begin=0, end=None):
    if end is None:
        end = len(arr) - 1

    def _quickSort(arr, begin, end):
        if begin >= end:
            return
        piv = partition(arr, begin, end)
        # recursively quicksort left and right parts of pivot
        _quickSort(arr, begin, piv - 1)
        _quickSort(arr, piv + 1, end)

    return _quickSort(arr, begin, end)


y = [1, 4, 5, 6, 2, 7, 8, 9, 15, 3, 20, 27, 200, 11]
quickSort(y)
print(y)
