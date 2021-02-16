from random import randint

arr_num = 10
array = [randint(0, 50) for _ in range(arr_num)]
print(array)


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2

    left_list = arr[:mid]
    right_list = arr[mid:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge_list(left_list, right_list)


def merge_list(list_1, list_2):
    result = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1

    result += list_1[i:]
    result += list_2[j:]
    return result


print(merge_sort(array))
