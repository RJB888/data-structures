"""Create insertion sort."""


def insertion_sort(potato):
    """Sort by insertion method."""
    for i in range(1, len(potato)):
        swap_index = i
        while swap_index > 0 and potato[swap_index] < potato[swap_index - 1]:
            potato[swap_index], potato[swap_index - 1] =\
                potato[swap_index - 1], potato[swap_index]
            swap_index -= 1
    return potato


if __name__ == "__main__":  # pragma: no cover
    import timeit as time
    import random
    reps = 100000
    rev = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    fwd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rand_sm = random.sample(range(100), 20)
    rand_lg = random.sample(range(2000), 500)
    t1 = time.timeit("bubble_sort(rev)",
                     number=reps,
                     setup="from __main__ import bubble_sort, rev")
    t2 = time.timeit("bubble_sort(fwd)",
                     number=reps,
                     setup="from __main__ import bubble_sort, fwd")
    t3 = time.timeit("bubble_sort(rand_sm)",
                     number=reps,
                     setup="from __main__ import bubble_sort, rand_sm")
    t4 = time.timeit("bubble_sort(rand_lg)",
                     number=reps,
                     setup="from __main__ import bubble_sort, rand_lg")

    print("Reversed list: ", t1)
    print("Ordered list: ", t2)
    print("Randomized small list: ", t3)
    print("Randomized large list: ", t4)
