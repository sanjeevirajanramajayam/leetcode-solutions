class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(['0000'])
        queue = deque([(0, '0000')])
        deadends = set(deadends)
        digits = list(string.digits)

        # print(digits)
        while queue:
            # print(queue)
            dist, num = queue.popleft()
            if num == target:
                return dist

            if num in deadends:
                continue

            num = list(num)
            for ch in range(len(num)):
                origChar = num[ch]

                #go up
                num[ch] = str((int(origChar) + 1) % 10)
                if "".join(num) not in visited:
                    queue.append((dist + 1, "".join(num)))
                    visited.add("".join(num))

                #go down
                num[ch] = str(((int(origChar) - 1) + 10) % 10)
                if "".join(num) not in visited:
                    queue.append((dist + 1, "".join(num)))
                    visited.add("".join(num))
                
                num[ch] = origChar
        # print(queue)
        return -1
