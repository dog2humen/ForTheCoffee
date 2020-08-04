# coding:utf8
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # 构造图
        for v_from, v_to in prerequisites:
            graph[v_from].append(v_to)

        for i in range(numCourses):
            if not self.helper(graph, visited, i):
                return False

        return True


    def helper(self, graph, visited, v):
        """ dfs """
        
        # 存在环的情况
        if visited[v] == -1:
            return False

        visited[v] = -1
        for v_next in graph[v]:
            if not self.helper(graph, visited, v_next):
                return False

        visited[v] = 1
        return True


if __name__ == '__main__':
    obj = Solution()
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    prerequisites = [[1,0]]
    res = obj.canFinish(numCourses, prerequisites)
    print(res)
