from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            n1 = target - nums[i]
            if n1 in nums[i+1:]:
                return [i, i + 1 + nums[i+1:].index(n1)]
