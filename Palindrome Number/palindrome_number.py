class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return True if x >= 0 and x == int(str(x)[::-1]) else False
