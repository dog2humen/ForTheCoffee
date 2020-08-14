# coding:utf8
class Solution:
    def isValid(self, s: str) -> bool:
        return self.isValid_v1(s)
    def isValid_v1(self, s: str) -> bool:
        """ use stack """
        if not s:
            return True
        maps = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack = []
        for ch in s:
            if ch in maps:
                stack.append(ch)
            else:
                cur_ch = stack.pop() if stack else '#'
                if maps.get(cur_ch) != ch:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    obj = Solution()
    s = ']'
    res = obj.isValid(s)
    print(res)
