# coding:utf8
from typing import List
from collections import defaultdict
import sys
import functools
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        #return self.respace_v1(dictionary, sentence)
        return self.respace_v2(dictionary, sentence)

    def respace_v1(self, dictionary: List[str], sentence: str) -> int:
        '''
            dp解法
            dp[i]表示sentence以i位置为结尾的最小匹配数
            状态转移方程:
                1. 若第i个字符不匹配, 则dp[i] = dp[i - 1] + 1
                2. 遍历前sentence的i-1个, 若以其中某个下标id为开头, 以i为结尾的单词在dictionary里(匹配到了), 则dp[i] = min(dp[idx], dp[i]) 
            初始化:
                dp长度为len(sentence) + 1, 预留空的匹配
                dp[0] = 0
        '''
        size = len(sentence)
        dp = [0 for _ in range(size + 1)]
        dp[0] = 0
        
        for i in range(1, size + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if sentence[j : i] in dictionary:
                    dp[i] = min(dp[j], dp[i])

        return dp[-1]

    def respace_v2(self, dictionary: List[str], sentence: str) -> int:
        '''
            dp解法
            使用字典树加速
            遍历前i - 1个时, 查询以第i为结尾的单词加速
        '''
        # 构建trie树
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        size = len(sentence)
        dp = [0 for _ in range(size + 1)]
        dp[0] = 0
        for i in range(1, size + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if trie.search(sentence[j : i]):
                    dp[i] = min(dp[j], dp[i])
        return dp[-1]




    def respace_v3(self, dictionary: List[str], sentence: str) -> int:
        '''
            暴力法, 枚举所有的上界和下界
        '''
        if len(sentence) == 0:
            return 0
        res = 0
        map_cache = defaultdict(list)
        for word in dictionary:
            map_cache[word[0]].append(word)
        print(map_cache)
        i = 0
        while i < len(sentence):
            if sentence[i] not in map_cache:
                res += 1
                i += 1
                continue

            print(sentence[i], map_cache.get(sentence[i]), len(map_cache.get(sentence[i])))

            if len(map_cache.get(sentence[i])) == 1:
                max_len = len(map_cache.get(sentence[i])[0])
            else:
                max_len = functools.reduce(lambda x, y : max(x if isinstance(x, int) else len(x), y if isinstance(y, int) else len(y)), map_cache.get(sentence[i]))
            flag, tmp_len = False, 0
            j = 0
            while j < max_len:
                if sentence[i : i + j + 1] in map_cache.get(sentence[i]):
                    flag = True
                    tmp_len = max(j + 1, tmp_len)
                j += 1
            # 匹配到
            if flag:
                i += tmp_len
            else:
                res += 1
                i += 1
            print('======', flag, tmp_len)
            
        return res

class Trie:

    def __init__(self):
        self.root = {}
        self.end_mark = '#'


    def insert(self, word: str) -> None:
        node = self.root
        for ch in word[::-1]:
            node = node.setdefault(ch, {})
        node[self.end_mark] = self.end_mark

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word[::-1]:
            if ch not in node:
                return False
            node = node[ch]
        return self.end_mark in node


    def startWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix[::-1]:
            if ch not in node:
                return False
            node = node[ch]
        return True

if __name__ == '__main__':
    obj = Solution()
    sentence = 'jesslookedjustliketimherbrother'
    dictionary = ["patk","mk","bgmuaukzpbp","tpakjawagaakakmpkkikjpbmppiiazkkdko","apoggddaakoadudmw","mugaxmgwkbptxmbmt","tijagbkixiwzdddbbjjgpk","goaotk","kk","xambkwpozgouaaamzgtpkojgdbxuwkjz","gmwo","bkbpdptkjxjgatdkukxmxkabkjmiuotiikb","ad","babtgmz","kujuak","ikimadpozaxozoaikttzamjakk","jjumibouto"]
    sentence = "bgmuaukzpbpkujuakpatk"
    dictionary = ["sssjjs","hschjf","hhh","fhjchfcfshhfjhs","sfh","jsf","cjschjfscscscsfjcjfcfcfh","hccccjjfchcffjjshccsjscsc","chcfjcsshjj","jh","h","f","s","jcshs","jfjssjhsscfc"]
    sentence = "sssjjssfshscfjjshsjjsjchffffs"
    dictionary = ["frrrbbrrbfrfqqbbbrb","qr","b","rf","qqbbbbfrqbrrqrffbrqqqbqqfqfrr","r","ffqq","bffbqfqqbrrrf","fq","qfr","fr","rqrrbfbfq","r","f","qbqbrbrbqfqbbbfbbbfbq","bqqbbbqrbbrf","f"]
    sentence = "bqqffbqbbfqrfrrrbbrrbfrfqqbbbrbfqfffffrfqfqfffffrrfqfrrqbqfrbfrqqrfrbrbbqbqbqqfqrfbfrfr"
    #sentence = 'jesslooked'
    #sentence = 'jesslojustliketimherbrother'
    #dictionary = ["looked","just","like","her","brother"]
    res = obj.respace(dictionary, sentence)
    print(res)
