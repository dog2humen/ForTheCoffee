# encoding=utf8
""""
336. 回文对
给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，
使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。

示例 1：
输入：["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]

示例 2：
输入：["bat","tab","cat"]
输出：[[0,1],[1,0]]
解释：可拼接成的回文串为 ["battab","tabbat"]
"""

class Node:
    def __init__(self):
        self.ch = [0] * 26
        self.flag = -1


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        return self.palindromePairs_v1(words)

    def palindromePairs_v1(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if self.check(words[i] + words[j]):
                    res.append([i, j])
        return res


    def check(self, words):
        if not words:
            return True

        left = 0
        right = len(words) - 1
        while left < right:
            if words[left] != words[right]:
                return False
            left += 1
            right -= 1
        return True


    # 字典树 
    def palindromePairs_v2(self, words):
        tree = [Node()]

        def insert(s, index):
            length = len(s)
            add = 0
            for i in range(length):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    tree.append(Node())
                    tree[add].ch[x] = len(tree) - 1
                add = tree[add].ch[x]
            tree[add].flag = index

        def findWord(s, left, right):
            add = 0
            for i in range(right, left - 1, -1):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    return -1
                add = tree[add].ch[x]
            return tree[add].flag

        def isPalindrome(s, left, right):
            length = right - left + 1
            return length < 0 or all(s[left + i] == s[right - i] for i in range(length // 2))

        n = len(words)
        for i, word in enumerate(words):
            insert(word, i)

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret




if __name__ == '__main__':
    s = Solution()
    print s.palindromePairs(["bat","tab","cat"])


