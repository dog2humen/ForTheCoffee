# encoding=utf8
"""
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left, right, max_length = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2*left)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0
        for i in range(len(s))[::-1]:
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2*left)
            elif left > right:
                left, right, = 0, 0
        return max_length

    def longestValidParentheses_stack(self, s):
        if not s:
            return 0
        max_length = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length


if __name__ == '__main__':
    s = Solution()
    print s.longestValidParentheses("))(()())")
    print s.longestValidParentheses(")()())")
    print s.longestValidParentheses("()(()")
    print s.longestValidParentheses_stack("))(()())")
    print s.longestValidParentheses_stack(")()())")
    print s.longestValidParentheses_stack("()(()")
