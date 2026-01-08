class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        counter = {}
        for i in range(len(hand)):
            counter[hand[i]] = counter.get(hand[i], 0) + 1
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(first, first + groupSize):
                if i not in counter:
                    return False
                counter[i] -= 1
                if counter[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True