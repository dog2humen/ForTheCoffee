# coding:utf8

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #candidates.sort()
        self.helper(candidates, target, 0, [], res)
        return res

    def helper(self, candidates, target, start, cur, res):

        if target == 0:
            res.append(cur[:])
            return

        for i in range(start, len(candidates)):
            #if target - candidates[i] < 0:
            #    break
            if target < 0:
                break
            self.helper(candidates, target - candidates[i], i, cur + [candidates[i]], res)





if __name__ == '__main__':
    obj = Solution()
    candidates = [2,3,6,7]
    candidates = [8, 7, 4, 3]
    target = 11
    res = obj.combinationSum(candidates, target)
    print(res)
