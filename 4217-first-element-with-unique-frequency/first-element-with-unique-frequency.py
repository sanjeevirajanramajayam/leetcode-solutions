class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqMap = {}
        for i in nums:
            freqMap[i] = freqMap.get(i, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for i in freqMap:
            buckets[freqMap[i]].append(i)

        for i in range(len(nums)):
            if len(buckets[freqMap[nums[i]]]) == 1:
                return nums[i]

        return -1
            