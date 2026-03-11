class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return ~n & (2 ** (len(bin(n)[2:])) - 1)