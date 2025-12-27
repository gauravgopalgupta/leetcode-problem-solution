class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for i in nums:
            if i not in ans:
                ans.append(i)
            else:
                ans.remove(i)

        return ans[0]
