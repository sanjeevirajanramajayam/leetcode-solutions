class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        b = [1] * len(nums)
        p = [i for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if b[j] + 1 > b[i]:
                        b[i] = b[j] + 1
                        p[i] = j
        # print(p)
        # print(b)
        maxIndex = -1
        maxVal = max(b)
        for i in range(len(nums)):
            if b[i] == maxVal:
                maxIndex = i
        ans = []
        ans.append(nums[maxIndex])
        curr = maxIndex
        next = p[curr]
        while curr != next:
            ans.append(nums[next])
            curr = next
            next = p[curr]
        return ans