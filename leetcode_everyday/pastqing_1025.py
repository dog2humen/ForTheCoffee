# coding:utf8
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


if __name__ == '__main__':
    obj = Solution()
    N = 4
    res = obj.divisorGame(N)
    print(res)
