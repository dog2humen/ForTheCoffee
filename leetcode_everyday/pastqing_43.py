# coding:utf8
import sys
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return self.multiply_v1(num1, num2)

    def multiply_v1(self, num1: str, num2: str) -> str:
        """ 双指针 """
        res = 0
        i = len(num1) - 1
        while i >= 0:
            carry = 0
            n1 = ord(num1[i]) - ord('0')
            j, k, tmp_res = len(num2) - 1, 0, 0
            while j >= 0:
                n2 = ord(num2[j]) - ord('0')
                tmp =  n1 * n2 + carry
                tmp_res = (tmp % 10) * (10 ** k) + tmp_res
                carry = tmp // 10
                j -= 1
                k += 1
            if carry > 0:
                tmp_res = carry * (10 ** k) + tmp_res

            res = tmp_res  * (10 ** (len(num1) - i - 1)) + res
            i -= 1

        return str(res)


if __name__ == '__main__':
    obj = Solution()
    num1 = '123'
    num2 = '456'
    res = obj.multiply(num1, num2)
    print(res)
	



