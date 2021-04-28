# coding:utf8
"""
    并查集数据结构
"""

class UnionFind(object):
    """
        并查集
    """

    def __init__(self):
        """
            使用字典来模拟各个节点
        """

        # 节点x 为key, 其父节点为value
        self.id = {}
        # 记录联通分量 
        self.count = 0
        # 记录每个节点树所包含的节点个数, 平衡性优化 
        self.size = {}


    def add(self, p):
        """
            添加一个节点
        """
        self.id[p] = p # 父节点指向自己
        self.size[p] = 1
        self.count += 1


    def find(self, p):
        """
            返回节点p的根节点
        """
        while self.id[p] != p:
            # 路径压缩
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return 

        # 小树接到大树下面, 使之较为平衡
        if self.size[rootP] > self.size[rootQ]:
            self.id[rootQ] = rootP
            self.size[rootP] += self.size[rootQ]
        else:
            self.id[rootP] = rootQ
            self.size[rootQ] += self.size[rootP]

        self.count -= 1
