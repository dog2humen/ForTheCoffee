# coding:utf8
from typing import List
class Solution:
    dirs = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, 1), (1, -1), (0, -1), (0, 1)]
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        #return self.updateBoard_v1(board, click)
        return self.updateBoard_v2(board, click)

    def updateBoard_v1(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row_start, col_start = click
        if board[row_start][col_start] == 'M':
            board[row_start][col_start] = 'X'
            return board

        rows, cols = len(board), len(board[0])
        self.dfs(row_start, col_start, board, rows, cols)
        return board

    def dfs(self, rowIdx, colIdx, board, rows, cols):

        if board[rowIdx][colIdx] != 'E':
            return
        
        mcount =  0
        for dx, dy in Solution.dirs:
            nrowIdx, ncolIdx = rowIdx + dx, colIdx + dy
            if 0 <= nrowIdx < rows  and 0 <= ncolIdx < cols and board[nrowIdx][ncolIdx] == 'M':
                mcount += 1

        if mcount == 0:
            board[rowIdx][colIdx] = 'B'
        else:
            board[rowIdx][colIdx] = str(mcount)
            return

        for dx, dy in Solution.dirs:
            nrowIdx, ncolIdx = rowIdx + dx, colIdx + dy
            if 0 <= nrowIdx < rows  and 0 <= ncolIdx < cols:
                self.dfs(nrowIdx, ncolIdx, board, rows, cols)

    def updateBoard_v2(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row_start, col_start = click
        if board[row_start][col_start] == 'M':
            board[row_start][col_start] = 'X'
            return board

        rows, cols = len(board), len(board[0])
        self.bfs(row_start, col_start, board, rows, cols)
        return board

    
    def bfs(self, rowIdx, colIdx, board, rows, cols):

        queue, visited = [], []
        queue.append((rowIdx, colIdx))
        visited.append((rowIdx, colIdx))
        while queue:
            x, y = queue.pop(0)
            if board[x][y] != 'E':
                continue
            mcount = 0
            for dx, dy in Solution.dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == 'M':
                    mcount += 1
            if mcount == 0:
                board[x][y] = 'B'
            else:
                board[x][y] = str(mcount)
                continue


            for dx, dy in Solution.dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.append((nx, ny))






if __name__ == '__main__':
    obj = Solution()
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    obj.updateBoard(board, click)
    for item in board:
        print(item)

