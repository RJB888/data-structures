"""Quick sort some list."""


def quick_sort(list_in, pivot, end):
    """Implement the quick sort."""
    first = pivot
    last = end
    fwd = pivot + 1
    if last - first < 2:
        return list_in
    while fwd <= end:
        while list_in[fwd] < list_in[pivot]:
            if fwd == last:
                break
            fwd += 1
        while list_in[end] > list_in[pivot]:
            if end == first:
                break
            end -= 1
        if fwd < end:
            list_in[end], list_in[fwd] = list_in[fwd], list_in[end]
        else:
            list_in[pivot], list_in[end] = list_in[end], list_in[pivot]
            return quick_sort(list_in, first, end - 1),\
                quick_sort(list_in, end + 1, last)
