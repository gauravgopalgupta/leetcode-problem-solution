# Time limit exceeded for this code.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_val = 0
        length = len(height)
        for i in range(0, length - 1):
            if height[i] * (length - i) <= max_val:
                continue
            for j in range(length-1, i, -1):
                cal = min(height[i], height[j]) * (j-i)
                max_val = max(max_val, cal)

        return max_val
