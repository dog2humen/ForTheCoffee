# encoding=utf8
import numpy as np


class Solution(object):
    # 初始化
    def __init__(self):
        self.total = 0
        self.return_list = []

    def solve_n_queens(self, n):
        arr = np.zeros(n * n, dtype=np.str_).reshape(n, n)
        arr[:] = "."
        self.find_queen(0, n, arr)
        return self.return_list, self.total

    # 递归回溯核心
    # param row : 当前行
    # param n   : n 皇后
    # param arr : 一种可能的排列
    def find_queen(self, row, n, arr):
        if row > n - 1:  # 递归终止条件
            self.total += 1
            self.return_list.append(self.print_queen(arr))
            return
        for column in range(n):
            if self.check_the_point(row, column, n, arr):
                arr[row][column] = "Q"
                self.find_queen(row + 1, n, arr)
                arr[row][column] = "."  # 上面 return , 会返回上一层 , 此时要把刚才设置为 Q 的位置复原

    @staticmethod
    def check_the_point(row, column, n, arr):
        # 上
        i, j = row, column
        while i >= 0:
            if arr[i][j] == "Q":
                return False
            i -= 1

        # 左上
        i, j = row, column
        while i >= 0 and j >= 0:
            if arr[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # 右上
        i, j = row, column
        while i >= 0 and j < n:
            if arr[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    @staticmethod
    def print_queen(arr):
        list_str = []
        for i in arr:
            list_str.append(''.join(i))
        return list_str


if __name__ == '__main__':
    s = Solution()
    all_queen_list, total_num = s.solve_n_queens(4)
    print "总共有 %d 种可能！！！\n" %total_num
    for count, one_queen_list in enumerate(all_queen_list):
        print "The %d" % (count+1)
        for row in one_queen_list:
             print row
        print '\n'

