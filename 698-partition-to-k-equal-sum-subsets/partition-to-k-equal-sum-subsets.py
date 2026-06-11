class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        visited = set()

        def fn(ind, currK, currSum):
            if currK == 1:
                return True

            if currSum == target:
                return fn(0, currK - 1, 0)

            prev = -1

            for i in range(ind, len(nums)):
                if i in visited:
                    continue

                if nums[i] == prev:
                    continue

                if currSum + nums[i] > target:
                    continue

                visited.add(i)

                if fn(i + 1, currK, currSum + nums[i]):
                    return True

                visited.remove(i)

                prev = nums[i]

                # bucket empty and first choice failed
                if currSum == 0:
                    break

            return False

        return fn(0, k, 0)