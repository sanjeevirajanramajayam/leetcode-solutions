class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def divisor(num):
            count = 0
            divisiorSum = 0
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    count += 1
                    divisiorSum += i
                    if num % (num / i) == 0 and num / i != i:
                        count += 1
                        divisiorSum += (num / i)
            if count == 4:
                return divisiorSum
            return 0

        DivisorSum = 0
        for i in range(len(nums)):
            DivisorSum += divisor(nums[i])
        return DivisorSum