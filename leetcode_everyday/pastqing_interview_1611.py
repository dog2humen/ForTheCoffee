# coding:utf8
from typing import List
class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [k * shorter]
        res = [shorter * (k - i) + longer * i for i in range(0, k + 1)]
        return res


if __name__ == '__main__':
    obj = Solution()
    shorter, longer, k = 1, 1, 100000
    res = obj.divingBoard(shorter, longer, k)
    print(res)

