# coding:utf8
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restoreIpAddresses_v1(s)
    def restoreIpAddresses_v1(self, s: str) -> List[str]:
        """思路: 回溯添加点的位置"""

        res = []
        self.helper(0, s, '', res)
        return res

    def helper(self, level, s, curIp, res):
        if level == 4:
            if not s:
                res.append(curIp[:-1])
            return
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.helper(level + 1, s[i:], curIp + s[:i] + '.', res)
                if s[0] == '0':
                    break


if __name__ == '__main__':
    obj = Solution()
    s = '25525511135'
    res = obj.restoreIpAddresses(s)
    print(res)

