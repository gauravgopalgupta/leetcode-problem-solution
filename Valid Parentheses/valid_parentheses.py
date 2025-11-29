class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        z = []
        i = -1
        for x in range(0, len(s)):
            if s[x] == ')':
                if i >= 0 and z[i] == '(':
                    z.pop()
                    i -= 1
                else:
                    i += 1
                    z.append(s[x])

            elif s[x] == '}':
                if i >= 0 and z[i] == '{':
                    z.pop()
                    i -= 1
                else:
                    i += 1
                    z.append(s[x])

            elif s[x] == ']':
                if i >= 0 and z[i] == '[':
                    z.pop()
                    i -= 1
                else:
                    i += 1
                    z.append(s[x])
            else:
                i += 1
                z.append(s[x])

        return True if i == -1 else False
