def merge_and_sort(arr1, arr2):
    arr = arr1 + arr2
    arr.sort()
    print(arr)


arr1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
arr2 = [23, 24, 25, 26, 27, 28, 29, 210, 211, 212, 213, 124, 125]

merge_and_sort(arr1, arr2)


def merge_and_sort_by_not_adding_new_list(list1, list2):
    for i in range(len(list2)):
        list1.append(list2[i])
    print(sorted(list1))


list1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list2 = [23, 24, 25, 26, 27, 28, 29, 210, 211, 212, 213, 124, 125]

merge_and_sort_by_not_adding_new_list(list1, list2)
