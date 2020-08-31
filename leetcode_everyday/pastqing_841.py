# coding:utf8
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        return self.canVisitAllRooms_v1(rooms)

    def canVisitAllRooms_v1(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True
        #return self.dfs_iter(rooms, 0)
        #return self.dfs_recursive(rooms, 0)
        return self.bfs(rooms, 0)
    
    def dfs_iter(self, rooms, start):
        visited, stack = set(), [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                for nextNode in rooms[node]:
                    if nextNode not in visited:
                        stack.append(nextNode)
        return len(rooms) == len(visited)

    def dfs_recursive(self, rooms, start, visited = None):
        if visited is None:
            visited = set()
        visited.add(start)
        for node in rooms[start]:
            if node not in visited:
                self.dfs_recursive(rooms, node, visited)
        return len(visited) == len(rooms)
    
    def bfs(self, rooms, start):
        queue, visited = [start], set()
        
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                for nextNode in rooms[node]:
                    if nextNode not in visited:
                        queue.append(nextNode)
        return len(rooms) == len(visited)


