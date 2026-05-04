class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        prefixArray = [0]
        for i in range(1, len(nums)):
            if i - 1 == 0 or abs(nums[i - 1] - nums[i - 2]) > abs(nums[i - 1] - nums[i]):
                prefixArray.append(prefixArray[-1] + 1)
                continue
            prefixArray.append(prefixArray[-1] + abs(nums[i] - nums[i - 1]))
        # print(prefixArray)

        suffixArray = [0] * (len(nums) )
        for i in range(len(nums) - 2, -1, -1):
            if i + 1 == len(nums) - 1 or abs(nums[i + 1] - nums[i + 2]) >= abs(nums[i + 1] - nums[i]):
                suffixArray[i] = (suffixArray[i + 1] + 1)
                # print('closest', i)
                continue
            suffixArray[i] = (suffixArray[i + 1] + abs(nums[i] - nums[i + 1]))
        # print(suffixArray)
        ans = []
        for start, end in queries:
            if start < end:
                ans.append(prefixArray[end] - prefixArray[start])
            elif start > end:
                # print(start, end, suffixArray, suffixArray[end], suffixArray[start])
                ans.append(suffixArray[end] - suffixArray[start])
            else:
                ans.append(0)
        
        return ans