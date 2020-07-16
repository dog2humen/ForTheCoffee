# coding:utf8
from typing import List
from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #return self.isBipartite_v1(graph)
        return self.isBipartite_v2(graph)

    def isBipartite_v1(self, graph: List[List[int]]) -> bool:
        '''
            dfs
            相邻节点不能在一个集合中
            从节点开始将节点和相连的节点做不同的标记
        '''
        visited = {}

        for i, val in enumerate(graph):
            if i not in visited:
                if not self.dfs(graph, i, 1, visited):
                    return False

        return True

    def dfs(self, graph, node, color, visited):
        # terminated
        if node in visited:
            if visited[node] != color:
                return False
            return True

        # current level
        visited[node] = color
        # 相邻节点
        for v in graph[node]:
            if not self.dfs(graph, v, -color, visited):
                return False
        return True

    def isBipartite_v2(self, graph: List[List[int]]) -> bool:
        '''
            bfs, 利用队列结构
        '''

        visited = {}
        for i, val in enumerate(graph):
            if i not in visited:
                if not self.bfs(graph, i, visited):
                    return False
        return True

        

    def bfs(self, graph, node, visited):
        queue = [(node, 1)]

        while queue:
            curNode, color = queue.pop(0)
            if curNode in visited:
                if visited[curNode] != color:
                    return False
                continue

            visited[curNode] = color
            for v in graph[curNode]:
                queue.append((v, -color))

        return True







if __name__ == '__main__':
    obj = Solution()
    graph = [[1,3], [0,2], [1,3], [0,2]]
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    res = obj.isBipartite(graph)
    print(res)


