class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # oldS = s[:]
        c = Counter(barcodes)
        heap = [(-x, ch) for ch, x in c.items()]
        s = []
        heapq.heapify(heap)
        temp = (1, -1)
        while heap:
            # print(heap)
            freq, char = heapq.heappop(heap)
            s.append(char)
            if temp[0] < 0:
                heapq.heappush(heap, temp)
            temp = (freq + 1, char)
        # print(s)
        return s