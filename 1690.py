"""
str(i, n) 代表str字符串的从i个字符往后数n个字符组成的新字符串
f(s) 代表最少的为识别字符个数
p(s) 如果s在词典中，返回0，如果不在词典中，返回s的长度

动态规划
第一个空格的位置n

len = str.len

f(str(0, len)) = min(
p(str(0, 1)) + f(str(1, len - 1)),
p(str(0, 2)) + f(str(2, len - 2)),
...
p(str(0, n)) + f(str(n, len - n)),
...
p(str(0, len - 1)) + f(str(len - 1, 1)),
p(str(0, len)) + f(str(len, 0))
)

特殊情况
str(x, 0) 代表空字符串
p("") = 0
f("") = 0
"""


class Solution(object):
    cacheFRes = {}

    def p(self, dictionary, s):
        """
        :param dictionary: set
        :param s: str
        :return: int
        """
        if len(s) == 0:
            return 0

        if s in dictionary:
            return 0
        else:
            return len(s)

    def f(self, dictionary, s):
        """
        :param dictionary: set
        :param s: str
        :return: int
        """
        if len(s) == 0:
            return 0

        if s in dictionary:
            return 0

        if s in self.cacheFRes:
            return self.cacheFRes[s]

        length = len(s)
        minRes = length

        for i in range(1, length + 1):
            pNumber = self.p(dictionary, s[0:i])
            if pNumber >= minRes:
                continue
            temp = pNumber + self.f(dictionary, s[i:length])
            if temp < minRes:
                minRes = temp

        self.cacheFRes[s] = minRes
        return minRes

    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        self.cacheFRes.clear()
        return self.f(set(dictionary), sentence)


# print(Solution().respace(["looked", "just", "like", "her", "brother"], "jesslookedjustliketimherbrother"))
print(Solution().respace(["luazbabxzlbbxzb", "cub", "h"], "bbbzubbcabubbubbuahzha"))
# for i in range(1, 4):
#     print(i)
