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
        if len(sentence) == 0:
            return 0

        self.res = 0
        self.helper(dictionary, sentence, 0, len(sentence) - 1)
        return self.res
    

    def helper(self, dictionary, sentence, start, end):

        # terminated

        # cur level
        if sentence[start : end + 1] not in dictionary:
            self.res += len(sentence[start : end + 1])
        else:
            start = end

        # 枚举起点和终点
        for i in range(start, len(sentence)):
            self.helper(dictionary, sentence, start, i)

        #return self.res



    def respace_v2(self, dictionary: List[str], sentence: str) -> int:
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
