# coding:utf8
from collections import defaultdict
class Solution:
    def numTrees(self, n: int) -> int:
        return self.numTrees_v1(n)
    def numTrees_v1(self, n: int) -> int:
        '''
            recursive 
            按照整数k构建bst, 当前整数k作为根, 1...k - 1 则为左子树, k + 1...n 为右子树
            以k为根节点的bst种数= 左子树种数 * 右子树种数
        '''
        count_res = defaultdict(int) 
        return self.helper(n, count_res)
    
    def helper(self, n, count_res):
        
        # terminated
        if n in count_res:
            return count_res.get(n)

        if n <= 1:
            return 1

        # current level
        total = 0
        # 依次选取根
        for i in range(1, n + 1):
            # 左子树比根小
            left_counts = self.helper(i - 1, count_res)
            # 右子树比根大
            right_counts = self.helper(n - i, count_res)
            total += left_counts * right_counts

        count_res[n] = total
        return total



if __name__ == '__main__':
    n = 3
    obj = Solution()
    res = obj.numTrees(n)
    print(res)

        

