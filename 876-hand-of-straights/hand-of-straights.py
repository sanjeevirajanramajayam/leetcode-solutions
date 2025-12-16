class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        counter = {}
        for i in hand:
            counter[i] = counter.get(i, 0) + 1
        heap = list(counter.keys())
        heapq.heapify(heap)
        while heap:
            smallest = heap[0]
            for i in range(smallest, smallest + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        return True