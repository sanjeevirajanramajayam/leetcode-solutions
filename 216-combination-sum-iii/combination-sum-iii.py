class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        visited = [0 for i in range(10)]
        ans = []
        def fn(left, currSum, arr):
            # print(left, currSum, arr)
            if left == k:
                if currSum == n:
                    ans.append(arr[:])  
                return
            start = 1
            if arr != []:
                start = arr[-1]
            for i in range(start, 10):
                if visited[i] == 0:
                    if currSum + i <= n:
                        visited[i] = 1
                        fn(left + 1, currSum + i, arr + [i])
                    visited[i] = 0
            
        fn(0, 0, [])
        return ans