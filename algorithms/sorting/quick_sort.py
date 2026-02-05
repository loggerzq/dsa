def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if end <= start:
        return
        # after this loop i will be > j
    i = start
    j = end
    pivot = arr[start]
    while i < j:
        # now sort that stuff
        while arr[i] < pivot:
            # this stops when it finds an element greater than pivot
            i += 1
        while arr[j] > pivot:
            j -= 1
        # meaning they have not crossed over yet
        if i <= j:
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    # thats why right array starts at i
    quick_sort(arr, start, j)
    quick_sort(arr, i, end)


if __name__ == "__main__":
    a = [5, 55, 6, -1]
    quick_sort(a)
    print(a)
