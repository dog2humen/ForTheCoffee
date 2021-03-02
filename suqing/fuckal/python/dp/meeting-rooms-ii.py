# coding:utf8
"""
    253. 会议室 II
    给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。
    示例 1：
    输入：intervals = [[0,30],[5,10],[15,20]]
    输出：2
    链接：https://leetcode-cn.com/problems/meeting-rooms-ii
"""
from typing import List
import heapq

class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        return self.minMeetingRooms_v1(intervals)

    def minMeetingRooms_v1(self, intervals: List[List[int]]) -> int:
        """
            思路: 每有一个新会议, 检查是否有空闲的房间
            1. 按照开始时间排序
            2. 构建一个最小堆, 将第一个会议的end时间加入堆中
            3. 对每个新会议, 取堆顶, 判断是否有空闲房间:
                a.若有空闲, 则将堆顶拿出, 将结束时间改为当前end, 加回堆中
                b.若无空闲, 新加一个房间, 将其加入堆中
        """

        if not intervals:
            return 0
        arr = sorted(intervals, key = lambda x:x[0])
        free_room = []
        heapq.heappush(free_room, arr[0][1])
        for item in arr[1:]:
            free_end = free_room[0]
            cur_start, cur_end = item
            if cur_start >= free_end:
                heapq.heappop(free_room)

            heapq.heappush(free_room, cur_end)

        return len(free_room)


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    intervals = [[13, 15], [1, 13]]
    obj = Solution()
    print(obj.minMeetingRooms(intervals))
