# encoding=utf8
"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combine_v1(n, k)

    def combine_v1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if not n or not k:
            return []

        res = []
        path = []
        return self.dfs(n, k, 1, res, path)

    def dfs(self, n, k, start, res, path):
        if len(path) == k:
            import copy
            res.append(copy.deepcopy(path))
            return

        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            print (1, path)
            self.dfs(n, k, i + 1, res, path)
            path.pop()
            print (2, path)

        return res


if __name__ == '__main__':
    s = Solution()
    print s.combine(4, 2)
