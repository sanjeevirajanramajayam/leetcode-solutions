class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        c = Counter(barcodes)

        heap = []

        for num, freq in c.items():
            heapq.heappush(heap, (-freq, num))
        # print(heap)
        ans = []
        temp = None

        while heap:
            freq, num = heapq.heappop(heap)
            ans.append(num)
            freq = -freq
            # print(ans, heap)
            if temp:
                heapq.heappush(heap, temp)
                temp = None
                
            if freq - 1 > 0:            
                if temp is None:
                    temp = ((-(freq - 1),num))
            # print(heap)
            
        return ans