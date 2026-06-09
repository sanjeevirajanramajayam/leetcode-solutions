class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def fn(ind, start, arr):
            if ind == k:
                ans.append(arr[:])
                return
            for i in range(start + 1, n + 1):
                fn(ind + 1, i, arr + [i])
        fn(0, 0, [])
        return ans