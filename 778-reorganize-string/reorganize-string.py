class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        heap = []
        for key in c:
            heapq.heappush(heap, (-c[key], key))
        heapq.heapify(heap)
        ans = ""
        temp = None
        # print(heap)
        while heap:
            # print(temp, heap, ans)

            freq, char = heapq.heappop(heap)
            ans += char

            if temp:
                heapq.heappush(heap, (temp[0], temp[1]))
                temp = None

            if freq + 1 < 0:
                temp = [freq + 1, char]
        # print(ans)
        if len(ans) != len(s):
            return ""
        return ans