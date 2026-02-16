class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adjList = [[] for i in range(n)]

        for startNode, endNode, weight in roads:
            adjList[startNode].append((endNode, weight))
            adjList[endNode].append((startNode, weight))
        
        distArray = [ float('inf') for i in range(n)]
        distArray[0] = 0
        ways = [0 for i in range(n)]
        ways[0] = 1
        pq = ([(0, 0)])

        while pq:
            dist, node = heapq.heappop(pq)
            if dist > distArray[node]:
                continue
            for newNode, newDist in adjList[node]:
                if dist + newDist < distArray[newNode]:
                    distArray[newNode] = dist + newDist
                    heapq.heappush(pq, (dist + newDist, newNode))
                    ways[newNode] = ways[node]
                elif dist + newDist ==  distArray[newNode]:
                    ways[newNode] += ways[node]
                
                # print(node, newNode, ways)
        
        return ways[-1] % (10 ** 9 + 7)
            