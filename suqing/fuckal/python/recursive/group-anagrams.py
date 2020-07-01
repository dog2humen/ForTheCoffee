# coding:utf8
# 49 https://leetcode-cn.com/problems/group-anagrams/

from typing import List
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for item in strs:
            key = ''.join(sorted(item))
            if key in res:
                res[key] += [item]
            else:
                res[key] = [item]
	return list(res.values())

