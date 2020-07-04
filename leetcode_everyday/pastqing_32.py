# coding:utf8

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return self.longestValidParentheses_v1(s)
	#return self.longestValidParentheses_v2(s)

    def longestValidParentheses_v1(self, s: str) -> int:
        stack = [-1] # 插入一个下标-1当做初始分割点
        res = 0
        for i, item in enumerate(s):
            if item == '(':
                stack.append(i)
            elif stack and item == ')': # match
                cur = stack.pop()
                if stack:
                    res = max(res, i - stack[-1])
                else:   # 插入分割点
                    stack.append(i)


        return res
	
    def longestValidParentheses_v2(self, s: str) -> int:
        pass
	

if __name__ == '__main__':
    input = '()(()'
    #input = '()(())'
    obj = Solution()
    res = obj.longestValidParentheses(input)
    print(res)
