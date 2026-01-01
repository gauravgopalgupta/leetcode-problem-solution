class Solution:
    def climbStairs(self, n: int) -> int:
        cal1 = 1
        cal2 = 2
        if n == 1:
            return cal1
        elif n == 2:
            return cal2
        else:
            i = 3
            while i <= n:
                temp = cal2
                cal2 = temp + cal1
                cal1 = temp
                i += 1
            return cal2
