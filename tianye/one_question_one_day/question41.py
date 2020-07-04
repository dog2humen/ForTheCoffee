# encoding=utf8
"""
剑指 Offer 41. 数据流中的中位数
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：

void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
示例 1：

输入：
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
输出：[null,null,null,1.50000,null,2.00000]
"""
import heapq


class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []  # 小顶堆，保存较大的一半或一半多一个，堆顶是最小的元素
        self.B = []  # 大顶堆，保存较小的一半，堆顶是最大的元素


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.A) != len(self.B):
            heapq.heappush(self.A, num)  # 新数据，在较大的一半A中走一遍，保证堆顶是最小的
            heapq.heappush(self.B, -heapq.heappop(self.A))  # 拿到较大一半中的最小值，给较小的一半B，保证 A，B 个数相等
        else:
            heapq.heappush(self.B, -num) # 新数据，在较小的一半B中走一遍，保证堆顶是最大的
            heapq.heappush(self.A, -heapq.heappop(self.B))  # 拿到较小一半中的最大值，给较大的一半A，保证 A 比 B 多一个

    def findMedian(self):
        """
        :rtype: float
        """
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
