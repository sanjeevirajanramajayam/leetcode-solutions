class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []
        for i in range(len(arr)):
            heapq.heappush(pq, (abs(arr[i] - x) ,arr[i]))
        # print(pq)
        ans = []
        while k > 0:
            ans.append(heapq.heappop(pq)[1])
            k -= 1

        return sorted(ans)