# coding:utf8
from typing import List
class Solution:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve_v1(board)
    def solve_v1(self, board: List[List[str]]) -> None:
        """从边界的O出发, 找联通的O"""
        if not board:
            return
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or j == 0 or i == rows - 1 or j == cols - 1) and board[i][j] == 'O':
                    self.helper(board, i, j, rows, cols)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


    def helper(self, board, rowIdx, colIdx, rows, cols):

        if rowIdx < 0 or colIdx < 0 or rowIdx >= rows or colIdx >= cols or board[rowIdx][colIdx] == 'X' or board[rowIdx][colIdx] == '#':
            return
        
        board[rowIdx][colIdx] = '#'

        for dx, dy in Solution.dirs:
            self.helper(board, rowIdx + dx, colIdx + dy, rows, cols)






if __name__ == '__main__':
    obj = Solution()
    board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]]
    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    print(board)
    obj.solve(board)
    print(board)
