class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            heapq.heappush(heap, (sqrt(points[i][0] ** 2 + points[i][1] ** 2), i))
        # print(heap)
        ans = []
        for i in range(k):
            ans.append(points[heapq.heappop(heap)[1]])
        return ans