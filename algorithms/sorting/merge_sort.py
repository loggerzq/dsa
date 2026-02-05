def merge(arr, start, middle, end):
    if arr[start] <= arr[middle]:
        return
    i = start  # left side
    j = middle  # right side
    temp = []
    while i < middle and j < end:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
            continue
        temp.append(arr[j])
        j += 1
    temp.extend(arr[i:middle])
    temp.extend(arr[j:end])
    arr[start:end] = temp


def merge_sort(arr, start, end):
    if (end - start) == 1:
        return

    # split
    middle = (start + end) // 2
    merge_sort(arr, start, middle)
    merge_sort(arr, middle, end)
    merge(arr, start, middle, end)


# my first solution
# def merge_sort(arr, start, end):
#     if len(arr[start:end]) == 1:
#         # no need te merge because its alone
#         return arr[start:end]
#
#     middle = (start + end) // 2
#     left = merge_sort(arr, start, middle)
#     right = merge_sort(arr, middle, end)
#     i, j = 0, 0
#     temp = []
#     while i < len(left) or j < len(right):
#         if j >= len(right) or (i < len(left) and left[i] <= right[j]):
#             temp.append(left[i])
#             i += 1
#             continue
#         temp.append(right[j])
#         j += 1
#     return temp


a = [5, 55, 6, -1]
merge_sort(a, 0, len(a))
print(a)
