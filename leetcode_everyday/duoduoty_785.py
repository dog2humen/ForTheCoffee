class Solution(object):
    # BFS 
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited = [0] * len(graph)

        for i in range(len(graph)):
            if visited[i] != 0:
                continue
            q = collections.deque([i])
            q.append(i)
            visited[i] = 1
            while q:
                cur_node = q.popleft()
                cur_color = visited[cur_node]
                neibour_color = - cur_color
                for neibour in graph[cur_node]:
                    if visited[neibour] == 0:
                        q.append(neibour)
                        visited[neibour] = neibour_color
                    elif visited[neibour] == cur_color:
                        return False
        return True
