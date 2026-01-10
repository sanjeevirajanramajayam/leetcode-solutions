class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxHeap = [-x for x in arr]
        heapq.heapify(maxHeap)
        rankMap = {}
        last_element = -1
        rank = 0
        while maxHeap:
            num = -heapq.heappop(maxHeap)    
            if last_element != num:
                rank += 1
                if num not in rankMap:
                    rankMap[num] = rank
                last_element = num
        maxRank = rank
        return [maxRank - rankMap[x] + 1 for x in arr]

