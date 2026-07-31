class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(heap)
        last_char = (-1, 0)
        s = ""
        temp = None
        while heap:
            freq, char = heapq.heappop(heap)
            if freq >= 0:
                continue
            s += char
            # print(s, freq, char, heap, temp, last_char)

            if temp:
                if temp[0] < 0:
                    heapq.heappush(heap, temp)
                temp = None
            
            if last_char[0] != char:
                last_char = (char, 1)
            else:
                last_char = (char, last_char[1] + 1)
            
            if last_char[1] == 2:
                temp = (freq + 1, char)
            else:
                if freq + 1 < 0:
                    heapq.heappush(heap, (freq + 1 , char))
        return s
            
            