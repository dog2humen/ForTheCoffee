# coding:utf8



def merge_sort(arr, left, right):
    """
        Complexcity: O(n log(n))
    """
    if left < right:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    tmp = [0] * (right - left + 1)
    
    i, j, k = left, mid + 1, 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        tmp[k] = arr[j]
        j += 1
        k += 1

    k = 0
    while k < len(tmp):
        arr[left + k] = tmp[k]
        k += 1


def merge_sort_2(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2

    left_arr = merge_sort_2(arr[:mid])
    right_arr = merge_sort_2(arr[mid:])
    return merge_2(left_arr, right_arr, arr.copy())

def merge_2(left, right, tmp):

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp[i + j] = left[i]
            i += 1
        else:
            tmp[i + j] = right[j]
            j += 1


    while i < len(left):
        tmp[i + j] = left[i]
        i += 1
    while j < len(right):
        tmp[i + j] = right[j]
        j += 1
    print(tmp)
    return tmp
if __name__ ==  '__main__':
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(arr)
    #merge_sort(arr, 0, len(arr) - 1)
    print(merge_sort_2(arr))
    print(arr)
