# encoding=utf8
"""
面试题 17.13. 恢复空格
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
在处理标点符号和大小写之前，你得先把它断成词语。
当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。

注意：本题相对原题稍作改动，只需返回未识别的字符数

示例：

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
"""
class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        if not dictionary:
            return len(sentence)
        if not sentence:
            return 0

        dictionary_dict = {}

        for i in dictionary:
            if i[0] in dictionary_dict:
                dictionary_dict[i[0]].append(i)
            else:
                dictionary_dict[i[0]] = [i]

        for key, value in dictionary_dict.items():
            dictionary_dict[key] = sorted(value, key=lambda i:len(i), reverse=True)

        print dictionary_dict

        res_num = 0
        pos = 0
        while pos < len(sentence):
            if sentence[pos] in dictionary_dict:
                flag = False
                for i in dictionary_dict[sentence[pos]]:
                    if sentence[pos:pos+len(i)] == i:
                        flag = True
                        pos += len(i)
                        break
                if not flag:
                    pos += 1
                    res_num += 1

            else:
                pos += 1
                res_num += 1

        return res_num

    def respace_dp(self, dictionary, sentence):
        if len(sentence) <= 0: return 0
        if len(dictionary) <= 0: return len(sentence)

        dp = [0] * (len(sentence) + 1)  # 最后一个0是哨兵
        for i in range(len(sentence)):
            dp[i] = dp[i - 1] + 1
            # 遍历所有单词，看能否和「以i为结尾的子串」一样
            for dic in dictionary:
                if (len(dic) <= i + 1) and sentence[i + 1 - len(dic):i + 1] == dic:
                    dp[i] = min(dp[i], dp[i - len(dic)])
        return dp[-2]




s = Solution()
dictionary = ["frrrbbrrbfrfqqbbbrb","qr","b","rf","qqbbbbfrqbrrqrffbrqqqbqqfqfrr",
              "r","ffqq","bffbqfqqbrrrf","fq","qfr","fr","rqrrbfbfq","r","f",
              "qbqbrbrbqfqbbbfbbbfbq","bqqbbbqrbbrf","f"]
sentence = "bqqffbqbbfqrfrrrbbrrbfrfqqbbbrbfqfffffrfqfqfffffrrfqfrrqbqfrbfrqqrfrbrbbqbqbqqfqrfbfrfr"

print s.respace(dictionary, sentence)




