# coding:utf8
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = 0
        i, j, k = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            tmp = n1 + n2 + carry
            res = (tmp % 10) * (10 ** k) + res
            carry = tmp // 10
            i -= 1
            j -= 1
            k += 1
        if carry > 0:
            res = carry * 10 ** k + res
        return str(res)

if __name__ == '__main__':
    obj = Solution()
    num1 = '219'
    num2 = '78'
    res = obj.addStrings(num1, num2)
    print(res)
