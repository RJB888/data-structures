"""Quick sort some list."""


def quick_sort(list_in):
    """Implement the quick sort."""
    pivot = 0
    fwd = 1
    end = len(list_in) - 1
    if len(list_in) > 1:
        while fwd < end:
            if list_in[fwd] >= list_in[pivot]:
                while list_in[end] > list_in[pivot]:
                    end -= 1
                # swap val at fwd point with val at end point
                list_in[end], list_in[fwd] = list_in[fwd], list_in[end]
                end -= 1
                fwd += 1
            else:
                fwd += 1
        while list_in[end] > list_in[pivot]:
            if list_in[end] == list_in[pivot]:
                end -= 1
                fwd += 1
            else:
                end -= 1
        list_in[end], list_in[pivot] = list_in[pivot], list_in[end]
        # recurse -- use list_in at [pivot + 1:end]
        return quick_sort(list_in[:end]) + list(list_in[end]) +\
            quick_sort(list_in[(end + 1):])
    else:
        return list_in
