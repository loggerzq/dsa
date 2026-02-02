def selection_sort(arr):
    last_unsorted_index = len(arr)-1
    for i in range(len(arr)):
        # loop to get max_val from 0 to last_unsorted_index
        max_val = 0 # index of max value initialized as the first element
        for j in range(last_unsorted_index+1):
            if arr[j] > arr[max_val]:
                max_val = j

        # swap the max_val to the last_unsorted_index
        arr[last_unsorted_index], arr[max_val] = arr[max_val], arr[last_unsorted_index]

        # then decrement the last unsorted index
        last_unsorted_index = last_unsorted_index - 1

    # this return is like the letter p in corps
    # its useless because list is a referenced type so you are editing the actual array
    # no need to return it
    return arr

if __name__ == "__main__":
    a = [1,5,4,3]
    print("Unsorted:")
    print(a)
    selection_sort(a)
    print("Sorted:")
    print(a)
