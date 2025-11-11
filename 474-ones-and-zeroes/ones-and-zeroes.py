class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        strlen = len(strs) 
        memoarr = [[[ -1 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(strlen + 1)]
        # print(memoarr)
        counts = []
        for s in strs:
            zero = s.count('0')
            one = s.count('1')
            counts.append((zero, one))

        def fn(index, zero, one):
            if zero > m:
                return float('-inf')

            if one > n:
                return float('-inf')

            if memoarr[index][zero][one] != -1:
                return memoarr[index][zero][one]

            if index == (len(strs)):
                return 0

            zeroNew, oneNew = counts[index]
            left = 1 + fn(index + 1, zero + zeroNew, one + oneNew)
            right = fn(index + 1, zero, one)
            memoarr[index][zero][one] = max(left, right)
            return memoarr[index][zero][one]
        return fn(0, 0, 0)
        # return maxLen[0]