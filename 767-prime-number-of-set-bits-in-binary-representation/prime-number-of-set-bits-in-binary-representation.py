class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        prime_set = set([2, 3, 5, 7, 11, 13, 17, 19])

        def count_set_bits(n):
            return sum(map(int, bin(n)[2:])) in prime_set
        count = 0
        for i in range(left, right + 1):
            if count_set_bits(i):
                count += 1
        return count