class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        @cache
        def fn(ind, target):
            if target == 0:
                return True

            if ind == 0:
                return arr[0] == target

            if arr[ind] <= target and fn(ind - 1, target - arr[ind]):
                return True

            return fn(ind - 1, target)

        return fn(len(arr) - 1, sum(arr) / 2)