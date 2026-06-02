class Solution:
    def countArrangement(self, n: int) -> int:
        cnt = 0
        def fn(ind, visited):
            # print(ind, visited)
            nonlocal cnt
            if ind == 0:
                # print(visited)
                cnt += 1
                return
            for i in range(1, n + 1):
                # print(i, ind % i, i % ind)
                if i not in visited and (ind % i == 0 or i % ind == 0):
                    # print(i)
                    visited.add(i)
                    fn(ind - 1, visited)
                    visited.remove(i)
        fn(n, set())
        return cnt