# coding:utf8

from typing import List
class Solution:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.exist_v1(board, word)

    def exist_v1(self, board: List[List[str]], word: str) -> bool:
        """ bfs """
        if not word:
            return False
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, word, i, j, rows, cols):
                    return True
        return False

    def dfs(self, board, word, rowIdx, colIdx, rows, cols, visited = None):
        
        if not visited:
            visited = set()

        if len(word) == 0:
            return True

        if rowIdx < 0 or rowIdx >= rows or colIdx < 0 or colIdx >= cols:
            return False
        
        #print(rowIdx, colIdx, board[rowIdx][colIdx], word, visited)

        if word[0] != board[rowIdx][colIdx]:
            return False

        visited.add((rowIdx, colIdx))
        res = False 

        for dx, dy in Solution.dirs:
            nrowIdx, ncolIdx = rowIdx + dx, colIdx + dy
            if (nrowIdx, ncolIdx) not in visited:
                res = res or self.dfs(board, word[1:], nrowIdx, ncolIdx, rows, cols, visited)

        visited.remove((rowIdx, colIdx))

        return res





if __name__ == '__main__':
    obj = Solution()
    board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']]
    word = 'ABCB'
    #word = 'ABCCED'
    board = [
            ['A', 'B'], 
            ['C', 'D']]
    word = 'CDBA'
    res = obj.exist(board, word)
    print(res)

