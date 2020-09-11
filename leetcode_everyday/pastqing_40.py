# coding:utf8

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.helper(candidates, target, 0, [], res)
        return res

    def helper(self, candidates, target, start, cur, res):

        if target == 0:
            res.append(cur[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if target - candidates[i] < 0:
                break
            self.helper(candidates, target - candidates[i], i + 1, cur + [candidates[i]], res)





if __name__ == '__main__':
    obj = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    res = obj.combinationSum2(candidates, target)
    print(res)
