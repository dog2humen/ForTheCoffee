# coding:utf8

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


def binary_search_left(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] >= target:
            hi = mid - 1
        else:
            lo = mid + 1

    if lo >= len(arr) or arr[lo] != target:
        return -1
    return lo

def binary_search_right(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] <= target:
            lo = mid + 1
        else:
            hi = mid - 1

    if hi < 0 or arr[hi] != target:
        return -1

    return hi


if __name__ == '__main__':
    arr = [0, 1, 1, 1, 2, 3, 4]
    print(binary_search(arr, 3))
    print(binary_search_left(arr, 1))
    print(binary_search_right(arr, 1))
