# coding:utf-8
# https://leetcode-cn.com/problems/generate-parentheses/ 


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            生成n对括号, 递归生成左括号, 右括号
        '''
        res = []
        self.helper(n, 0, 0, '', res)
        return res

    def helper(self, n, left_num, right_num, curS, res):
        
        if left_num == n and right_num == n:
            res.append(curS)
            return 

        if left_num < n:
            self.helper(n, left_num + 1, right_num, curS + '(', res)

        if right_num < left_num:
            self.helper(n, left_num, right_num + 1, curS + ')', res)

if __name__ == '__main__':
    obj = Solution()
    n = 3
    res = obj.generateParenthesis(3)
    print(res)
