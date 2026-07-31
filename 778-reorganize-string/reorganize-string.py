class Solution:
    def reorganizeString(self, s: str) -> str:
        oldS = s[:]
        c = Counter(s)
        heap = [(-x, ch) for ch, x in c.items()]
        s = ""
        heapq.heapify(heap)
        temp = (1, -1)
        while heap:
            # print(heap)
            freq, char = heapq.heappop(heap)
            s += char
            if temp[0] < 0:
                heapq.heappush(heap, temp)
            temp = (freq + 1, char)
        # print(s)
        if len(s) != len(oldS):
            return ""
        return s