class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i] - heights[i + 1]
            
            if diff >= 0:
                continue
            else:
                heapq.heappush(heap, diff)
                bricks += diff
                if bricks < 0:
                    if ladders == 0:
                        return i
                    ladders -= 1
                    bricks += -heapq.heappop(heap)
                # print(bricks, heap)
        return len(heights) - 1
                