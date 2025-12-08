class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                sqr_sum = int((i ** 2 + j ** 2)**0.5)
                if sqr_sum * sqr_sum == i ** 2 + j ** 2 and sqr_sum <= n:
                    count += 1
        return count