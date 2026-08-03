class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-c, 'c', 0), (-b, 'b', 0), (-a, 'a', 0)]
        heapq.heapify(heap)
        ans = ""
        temp = None
        
        while heap:
            # print(heap, ans, temp)
            freq, char, time = heapq.heappop(heap)
            if freq == 0:
                continue
            ans += char
            if temp:
                heapq.heappush(heap, (temp[0], temp[1], temp[2]))
                temp = None
            if time == 1:
                if freq + 1 < 0:
                    temp = (freq + 1, char, 0)
            else:
                if freq + 1 < 0:
                    heapq.heappush(heap, (freq + 1, char, time + 1))
        return ans