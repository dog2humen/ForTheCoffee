# coding:utf8
from typing import List
class Solution:
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        return self.floodFill_v1(image, sr, sc, newColor)
    def floodFill_v1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image

        p = image[sr][sc]
        if p == newColor:
            return image
        
        rows, cols = len(image), len(image[0])
        self.dfs(image, sr, sc, rows, cols, newColor, p)
        return image

    def dfs(self, image, rowIdx, colIdx, rows, cols, newcolor, p):

        if rowIdx < 0 or colIdx < 0 or rowIdx >= rows or colIdx >= cols or image[rowIdx][colIdx] != p:
            return
        image[rowIdx][colIdx] = newcolor
        for dx, dy in Solution.DIRS:
            self.dfs(image, rowIdx + dx, colIdx + dy, rows, cols, newcolor, p)
