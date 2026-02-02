def insertion_sort(arr):
    # loop for first_index_of_unsorted array and new_element
    for i in range(1,len(arr)):
        new_element = arr[i]
        # loop through the sorted array until -1 or the elements are greater than new element
        j = i - 1 # left of first_index_of_unsorted is the last element of sorted array
        while j >= 0 and arr[j] > new_element:
            # shift values to the right 
            arr[j+1] = arr[j]
            j -= 1

        # why j+1
        # when j = -1 it will be 0
        # AND when arr[j] <= new_element 
        # eg. [-1,10, 10]
        # and j = 0 and new_element = 5
        # you want to put the value to the right
        arr[j+1] = new_element

if __name__ == "__main__": 
    a = [5,1,4,3]
    print(f"Unsorted: {a}")
    insertion_sort(a)
    print(f"Sorted: {a}")

