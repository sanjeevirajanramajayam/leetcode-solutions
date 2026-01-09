class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        time = 0
        queue = deque()
        counter = {}
        for i in range(len(tasks)):
            counter[tasks[i]] = counter.get(tasks[i], 0) + 1
        maxHeap = [-x for x in (counter.values())]
        heapq.heapify(maxHeap)
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt != 0:
                    queue.append([cnt, time + n])
            if queue and queue[0][1] == time:
                cnt, _ = queue.popleft()
                heapq.heappush(maxHeap, cnt)

        return time