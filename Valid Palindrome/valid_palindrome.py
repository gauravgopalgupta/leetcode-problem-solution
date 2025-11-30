class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = ''.join(letter.lower() for letter in s if letter.isalnum())
        return s == s[::-1]
