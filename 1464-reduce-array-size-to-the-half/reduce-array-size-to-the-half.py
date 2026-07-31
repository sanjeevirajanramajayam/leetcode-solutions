class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        maxHeap = [(-x, ch) for ch, x in c.items()]
        heapq.heapify(maxHeap)
        length = len(arr)
        halfLen = length / 2
        cnt = 0
        while length > halfLen:
            lossFreq = -heapq.heappop(maxHeap)[0]
            # print(maxHeap, lossFreq)
            length -= lossFreq
            cnt += 1
        return cnt