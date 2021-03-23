# coding:utf8
import sys
def insert_sort(arr):
    """
        Complexity: O(n^2)
    """
    for i in range(len(arr)):
        cur = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cur:
            arr[pos] = arr[pos - 1]
            pos -= 1

        arr[pos] = cur



def insert_sort_2(arr):
    for i in range(len(arr) - 1):
        cur = arr[i + 1]
        pos = i
        while cur < arr[pos]:
            arr[pos + 1] = arr[pos]
            if pos == 0:
                pos -= 1
                break
            pos -= 1

        arr[pos + 1] = cur 

if __name__ == '__main__':
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    insert_sort_2(arr)
        
