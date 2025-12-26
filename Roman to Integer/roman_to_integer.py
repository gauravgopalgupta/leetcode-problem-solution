class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_num = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        pre = 0
        ans = 0
        for i in s[::-1]:
            if roman_num[i] < pre:
                ans -= roman_num[i]
            else:
                ans += roman_num[i]
            pre = roman_num[i]

        return ans
