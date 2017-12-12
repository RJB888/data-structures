"""Create a merge sort."""


def merge(arr):
    """Take an array and start merge sort on it."""
    if not arr:
        return []
    merge_recurser(arr, 0, (len(arr) - 1))
    return arr


def merge_recurser(arr, first, last):
    """Split array in half and call merge on halves."""
    if first < last:
        middle = (first + last) // 2
        merge_recurser(arr, first, middle)
        merge_recurser(arr, middle + 1, last)
        merge_sorter(arr, first, middle, last)


def merge_sorter(arr, first, middle, last):
    """Sort and re-merge numbers into array."""
    l_side = arr[first:middle + 1]
    r_side = arr[middle + 1: last + 1]
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


if __name__ == "__main__":  # pragma: no cover
    import timeit as time
    import random
    reps = 10000
    rev = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    fwd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rand_sm = random.sample(range(100), 20)
    rand_lg = random.sample(range(2000), 500)
    t1 = time.timeit("merge(rev)",
                     number=reps,
                     setup="from __main__ import merge, rev")
    t2 = time.timeit("merge(fwd)",
                     number=reps,
                     setup="from __main__ import merge, fwd")
    t3 = time.timeit("merge(rand_sm)",
                     number=reps,
                     setup="from __main__ import merge, rand_sm")
    t4 = time.timeit("merge(rand_lg)",
                     number=reps,
                     setup="from __main__ import merge, rand_lg")

    print("Reversed list: ", t1)
    print("Ordered list: ", t2)
    print("Randomized small list: ", t3)
    print("Randomized large list: ", t4)
