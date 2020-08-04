# encoding=utf8
"""
207. 课程表
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？



示例 1:
输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

示例 2:
输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

提示：
输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5
"""
from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        return self.canFinish_v1(numCourses, prerequisites)

    # 邻接表 + BFS
    def canFinish_v1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_course = [0 for _ in range(numCourses)]   # 每个课程的入度数
        course_pre_courses = [[] for _ in range(numCourses)]  # 邻接表：每个前置课程对应的所有后置课程
        for cur, pre in prerequisites:
            in_course[cur] += 1
            course_pre_courses[pre].append(cur)

        queue = deque()
        for i in range(numCourses):
            if not in_course[i]: queue.append(i)  # 没有前置课程的课程入队列

        # BFS
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in course_pre_courses[pre]:
                in_course[cur] -= 1
                if not in_course[cur]: queue.append(cur)

        return not numCourses

    # 邻接表 + DFS
    # 1、邻接表的构造
    # 2、DFS 的退出条件，循环体，后续处理
    def canFinish_v1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(i, course_pre_courses, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            
            flags[i] = 1
            for j in course_pre_courses[i]:
                if not dfs(j, course_pre_courses, flags):
                    return False
            
            flags[i] = -1
            return True


        course_pre_courses = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            course_pre_courses[pre].append(cur)
        
        for i in range(numCourses):
            if not dfs(i, course_pre_courses, flags): return False
        
        return True



if __name__ == '__main__':
    s = Solution()
    print s.canFinish(2, [[1,0],[0,1]])

