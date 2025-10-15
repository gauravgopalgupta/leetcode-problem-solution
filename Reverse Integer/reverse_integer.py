class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = False
        if x < 0:
            y = True
            x = abs(x)
        x = str(x)[::-1]
        if y:
            x = 0 - int(x)
        else:
            x = int(x)

        if (x < -2147483648) or (x > 2147483647):
            return 0
        else:
            return x
