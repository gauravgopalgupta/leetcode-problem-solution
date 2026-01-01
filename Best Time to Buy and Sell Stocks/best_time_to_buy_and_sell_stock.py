from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        num = prices[0]
        length = len(prices)
        for i in range(1, length):
            val = max(prices[i:length])
            ans1 = max(0, (val-num))
            ans = max(ans, ans1)
            num = prices[i]
        return ans
