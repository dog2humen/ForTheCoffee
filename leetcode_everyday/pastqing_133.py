# coding:utf8
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """ 连通图的遍历 """
        return self.cloneGraph_v1(node)
    def cloneGraph_v1(self, node: 'Node') -> 'Node':
        """ dfs """
        memo = {}

        def dfs(node):
            # terminated
            if node is None:
                return

            if node in memo:
                return memo[node]
            # current level
            new_node = Node(node.val, [])
            memo[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))

            return new_node
        
        return dfs(node)


    def cloneGraph_v2(self, node: 'Node') -> 'Node':
        """ bfs """




