# encoding=utf8
class Solution(object):
    # dfs method: out of time
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        return self.dfs(dungeon, len(dungeon), len(dungeon[0]), 0, 0)

    def dfs_out_of_time(self, dungeon, m, n, i, j):
        # 递归终止条件
        if i == m - 1 and j == n - 1:
            return max(1 - dungeon[i][j], 1)

        if i == m - 1:
            return max(self.dfs_out_of_time(dungeon, m, n, i, j + 1) - dungeon[i][j], 1)

        if j == n - 1:
            return max(self.dfs_out_of_time(dungeon, m, n, i + 1, j) - dungeon[i][j], 1)

        return max(min(self.dfs_out_of_time(dungeon, m, n, i + 1, j), self.dfs_out_of_time(dungeon, m, n, i, j + 1)) - dungeon[i][j], 1)

    # todo dfs method with memory

    # dp method
    def calculateMinimumHP_DP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon:
            return 0
        m = len(dungeon)
        n = len(dungeon[0])
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if i == m - 1 and j == n - 1:
                    dungeon[i][j] = max(1 - dungeon[i][j], 1)
                elif i == m -1:
                    dungeon[i][j] = max(dungeon[i][j+1] - dungeon[i][j], 1)
                elif j == n - 1:
                    dungeon[i][j] = max(dungeon[i+1][j] - dungeon[i][j], 1)
                else:
                    dungeon[i][j] = max(min(dungeon[i+1][j], dungeon[i][j+1]) - dungeon[i][j], 1)
        return dungeon[0][0]
