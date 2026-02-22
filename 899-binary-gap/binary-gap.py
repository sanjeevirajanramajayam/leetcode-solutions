class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        strk = 0
        max_strk = 0
        seen = False
        while n != 0:
            last_bit = n & 1
            if last_bit:
                if seen:
                    max_strk = max(max_strk, strk)
                    strk = 1
                elif not seen:
                    seen = True
                    strk += 1
            else:
                if seen:
                    strk += 1
            n = n >> 1
        return max_strk