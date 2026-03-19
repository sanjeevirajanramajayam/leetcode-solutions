class Solution(object):
    def minCost(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        freqMapAll = {}
        freqMap1 = {}
        for i in range(len(nums1)):
            freqMap1[nums1[i]] = freqMap1.get(nums1[i], 0) + 1
            freqMapAll[nums1[i]] = freqMapAll.get(nums1[i], 0) + 1


        freqMap2 = {}
        for i in range(len(nums2)):
            freqMap2[nums2[i]] = freqMap2.get(nums2[i], 0) + 1
            freqMapAll[nums2[i]] = freqMapAll.get(nums2[i], 0) + 1
        
        if freqMap1 == freqMap2:
            return 0

        for i in freqMapAll:
            if freqMapAll[i] % 2 != 0:
                return -1
        ops = 0
        for i in freqMapAll:
            freq1 = freqMap1.get(i, 0)
            freq2 = freqMap2.get(i, 0)
            print(freq1, freq2)
            if freq1 != freq2:
                needed = (freq2 + freq1) / 2
                ops += abs(needed - freq1) 

        return ops / 2
