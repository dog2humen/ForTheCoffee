# coding:utf8

def quickSort(arr, left, right):
    if left < right:
        pivot = partitions(arr, left, right)
        quickSort(arr, left, pivot - 1)
        quickSort(arr, pivot + 1, right)


def partitions(arr, left, right):
    wall = left

    for pos in range(left, right):
        if arr[pos] < arr[right]:
            arr[wall], arr[pos] = arr[pos], arr[wall]
            wall += 1

    arr[wall], arr[right] = arr[right], arr[wall]

    return wall



if __name__ == '__main__':
    arr = [9, 8, 7, 5, 4, 2]
    print(arr)
    quickSort(arr, 0, len(arr) - 1)
    print(arr)

