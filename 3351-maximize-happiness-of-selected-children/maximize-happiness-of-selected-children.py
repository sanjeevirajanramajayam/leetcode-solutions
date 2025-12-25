class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness = sorted(happiness, reverse=True)
        decrement = 0
        maxHap = 0
        for i in range(k):
            curHap = happiness[i] - decrement
            if curHap < 0:
                curHap = 0
            maxHap += curHap
            decrement += 1
        return maxHap