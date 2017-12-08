"""Implement a bubble sort."""


def bubble_sort(list):
    """Bubble sort."""
    if not list:
        raise IndexError("Cannot use an empty list.")
    swap = True
    while swap:
        swap = False
        for i in range(1, len(list)):
            if list[i] < list[i - 1]:
                temp = list[i]
                list[i] = list[i - 1]
                list[i - 1] = temp
                swap = True
    return list
