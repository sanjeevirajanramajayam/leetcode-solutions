class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_val = 0
        max_val = 0
        for i in range(len(s)):
            if s[i] == '(':
                min_val += 1
                max_val += 1
            elif s[i] == ')':
                min_val -= 1
                max_val -= 1
            else:
                min_val -= 1
                max_val += 1
            if min_val < 0:
                min_val = 0
            if max_val < 0:
                return False
        return min_val == 0