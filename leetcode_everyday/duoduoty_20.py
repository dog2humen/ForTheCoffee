class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        dict = {'(':')','[':']','{':'}', '-1':'-1'}
        stack = ['-1']
        for c in s:
            if c in dict:
                stack.append(c)
            elif dict[stack.pop()] != c:
                return False
        
        return len(stack) == 1
