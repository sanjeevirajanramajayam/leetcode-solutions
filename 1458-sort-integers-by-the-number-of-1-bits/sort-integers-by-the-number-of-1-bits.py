class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        def fn(a):
            count = 0
            while a != 0:
                last_digit = a & 1
                if last_digit:
                    count += 1
                a = a >> 1
            return count
    
        arr = sorted(arr, key=lambda x: (fn(x), x))

        return arr