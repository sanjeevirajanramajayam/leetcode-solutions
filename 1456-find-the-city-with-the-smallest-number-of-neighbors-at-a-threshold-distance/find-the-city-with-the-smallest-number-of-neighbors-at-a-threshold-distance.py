class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        adjList = [[] for i in range(n)]
        for start, end, wt in edges:
            adjList[start].append((end, wt))
            adjList[end].append((start, wt))
        print(adjList)
        def shortestDist(src):
            minHeap = [(0, src)]
            distArray = [float('inf') for i in range(n)]
            distArray[src] = 0
            visited = set()
            while minHeap:
                dist, src = heapq.heappop(minHeap)
                for endNode, wt in adjList[src]:
                    if distArray[src] + wt < distArray[endNode]:
                        distArray[endNode] = distArray[src] + wt
                        if distArray[endNode] <= distanceThreshold:
                            visited.add(endNode)
                        heapq.heappush(minHeap, (distArray[endNode], endNode))
            # print(distArray)
            return len(visited)
        cur_min, node = float('inf'), -1
        for i in range(n):
            if shortestDist(i) <= cur_min:
                cur_min = shortestDist(i)
                node = i
        return node