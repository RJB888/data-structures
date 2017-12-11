"""Create a merge sort."""


def merge_controller(arr):
    """Take an array and start merge sort on it."""
    merge_recurser(arr, 0, (len(arr) - 1))


def merge_recurser(arr, first, last):
    """Split array in half and call merge on halves."""
    if first < last:
        middle = (first + last) // 2
        merge_recurser(arr, first, middle)
        merge_recurser(arr, middle + 1, last)
        merge_sorter(arr, first, middle, last)


def merge_sorter(arr, first, middle, last):
    """Sort and re-merge numbers into array."""
    l_side = arr[first:middle]
    r_side = arr[middle:last + 1]
    l_side.append(float('inf'))
    r_side.append(float('inf'))
    l_idx = r_idx = 0

    for idx in range(first, last + 1):
        if l_side[l_idx] <= r_side[r_idx]:
            arr[idx] = l_side[l_idx]
            l_idx += 1
        else:
            arr[idx] = r_side[r_idx]
            r_idx += 1
