class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = {}
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1
        maxHeap = [-x for x in counter.values()]
        queue = deque()
        heapq.heapify(maxHeap)
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                task = -heapq.heappop(maxHeap)
                if task - 1 > 0:   
                    queue.append((task - 1, time + n))

            if queue and queue[0][1] == time:
                task, _ = queue.popleft()
                heapq.heappush(maxHeap, -task)
        return time
