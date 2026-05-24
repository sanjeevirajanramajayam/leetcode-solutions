class Solution:
    def rob(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        n = len(arr)
        dp = [-1] * (n)
        temp = arr
        arr = arr[1:]
        ans = arr[0]

        curr = arr[0]
        prev = arr[0]
        previ = arr[0]
        dp[0] = arr[0]
        for ind in range(1, n - 1):
            take = arr[ind]
            if ind - 2 >= 0:
                take = previ + arr[ind]
            not_take = prev
            curr = max(take, not_take)
            previ = prev
            prev = curr

        ans = max(ans, curr)

        arr = temp
        arr.pop()

        curr = arr[0]
        prev = arr[0]
        previ = arr[0]
        dp[0] = arr[0]
        for ind in range(1, n - 1):
            take = arr[ind]
            if ind - 2 >= 0:
                take = previ + arr[ind]
            not_take = prev
            curr = max(take, not_take)
            previ = prev
            prev = curr

        ans = max(ans, curr)
        return ans
