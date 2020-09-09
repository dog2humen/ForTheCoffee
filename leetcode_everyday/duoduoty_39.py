# encoding=utf8
"""
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

提示：
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combinationSum_v1(candidates, target)

    def combinationSum_v1(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        return self.dfs(candidates, target, 0, res, path, 0)

    def dfs(self, candidates, target, depth_sum, res, path, begin):
        if depth_sum == target:
            import copy
            res.append(copy.deepcopy(path))
            return

        if depth_sum > target:
            return

        for i in range(begin, len(candidates)):
            depth_sum += candidates[i]
            path.append(candidates[i])
            self.dfs(candidates, target, depth_sum, res, path, i)
            depth_sum -= candidates[i]
            path.pop()
        return res


if __name__ == '__main__':
    s = Solution()
    print s.combinationSum([2,3,5], 8)
