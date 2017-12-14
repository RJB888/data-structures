"""Quick sort some list."""


def quick_sort(list):
    if inputlen > 1:
        while fwd < end:
            if list[fwd] > list[pivot]:
                while list[end] > list[pivot]:
                    end -= 1
                swap list[end] / list[fwd]
                end -= 1
                fwd += 1

            else:
                fwd += 1
        if list[end] < list[pivot]:
            swap end/pivot
    recurse -- use list at [pivot + 1:end]
    (( return recurse(small side) + pivot + recurse(large side)  ))
    else:
        return list
