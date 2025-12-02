class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        hashmap = {}
        count = 0
        pairCount = 0
        traps = 0
        for i in range(len(points)):
            hashmap[points[i][1]] = hashmap.get(points[i][1], 0) + 1
        for i in list(hashmap.values()):
            if i >= 2:
                w = i * (i - 1) // 2
                traps = (traps + pairCount * w) 
                pairCount += w
        return traps % (10**9 + 7)
