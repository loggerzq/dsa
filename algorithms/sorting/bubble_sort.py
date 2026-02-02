def bubble_sort(arr):
    last_unsorted_index = len(arr) - 1
    for i in range(len(a)):
        for i in range(last_unsorted_index):
            if a[i] > a[i+1]:
                # swap or bubble the value so it goes to the top
                a[i+1], a[i] = a[i], a[i+1]
        last_unsorted_index = last_unsorted_index - 1
    return arr


if __name__ == "__main__":
    a = [1,5,4,3]
    print("Unsorted:")
    print(a)
    bubble_sort(a)
    print("Sorted:")
    print(a)
