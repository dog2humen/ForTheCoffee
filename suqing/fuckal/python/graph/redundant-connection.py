# coding:utf8
"""
    684. 冗余连接
    在本问题中, 树指的是一个连通且无环的无向图。
    输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

    结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

    返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3

    链接：https://leetcode-cn.com/problems/redundant-connection
"""

from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        return self.findRedundantConnection_v1(edges)

    def findRedundantConnection_v1(self, edges: List[List[int]]) -> List[int]:
        """
            并查集思路:
            判断冗余, 即判断是否有环, 即判断新加入的边的两个节点是否有共同的祖先
            如果有共同的祖先, 则这条边是冗余的
            如果没有共同的祖先, 则将这条边加入树中
        """
        node_counts = len(edges)
        ids = list(range(node_counts + 1))
        res = []
        for p, q in edges:
            if self._find(ids, p) != self._find(ids, q):
                self._union(ids, p, q)
            else:
                return [p, q]

        return res

    def _find(self, ids, p):
        while ids[p] != p:
            ids[p] = ids[ids[p]]
            p = ids[p]
        return p

    def _union(self, ids, p, q):
        rootP = self._find(ids, p)
        rootQ = self._find(ids, q)
        ids[rootP] = rootQ



if __name__ == '__main__':
    edges = [[1, 2], [1, 3], [2, 3]]
    obj = Solution()
    print(obj.findRedundantConnection(edges))
