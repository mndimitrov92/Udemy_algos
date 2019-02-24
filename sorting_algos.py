def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr


def selection_sort(arr):
    for i in range(len(arr)-1):
        idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        if idx != i:
            swap(arr, idx, i)
    return arr


def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            swap(arr, j, j-1)
            j -= 1
    return arr


def quick_sort(arr, low, high):
    if low >= high:
        return
    pivot_idx = partitition(arr, low, high)
    quick_sort(arr, low, pivot_idx-1)
    quick_sort(arr, pivot_idx+1, high)


def partitition(arr, low, high):
    pivot_idx = (low + high) // 2
    swap(arr, pivot_idx, high)

    i = low
    for j in range(low, high):
        if arr[j] <= arr[high]:
            swap(arr, i, j)
            i += 1
    swap(arr, i, high)

    return i


def merge_sort(arr):
    if len(arr) == 1:
        return
    middle_index = len(arr) // 2
    left_half = arr[:middle_index]
    right_half = arr[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        k += 1
        i += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        k += 1
        j += 1


if __name__ == "__main__":
    arr = [4, 3, 2, 0, 9, 7, -1, 5]
    # print bubble_sort(arr)
    # print selection_sort(arr)
    # print insertion_sort(arr)
    # quick_sort(arr, 0, len(arr)-1)
    merge_sort(arr)
    print arr
