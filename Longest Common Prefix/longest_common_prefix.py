class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = strs[0]
        min_len = len(strs[0])
        for i in range(1, len(strs)):
            if min_len <= 0:
                break
            min_len = min(min_len, len(strs[i]))
            ans = ans[:min_len]
            while (min_len >= 0) and (ans != strs[i][:min_len]):
                min_len -= 1
                ans = ans[:min_len]        
        return ans
