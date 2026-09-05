class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = deque([(0, start)])
        visited = set()
        while queue:
            # print(queue)
            dist, val = queue.popleft()
            if val == goal:
                return dist
            if val in visited:
                continue
            visited.add(val)
            if not (0 <= val <= 1000):
                continue
            
            for i in range(len(nums)):
                queue.append((dist + 1, val + nums[i]))
                queue.append((dist + 1, val - nums[i]))
                queue.append((dist + 1, val ^ nums[i]))
        return -1
