class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        longest = float('-inf')
        hash = {}
        for i in range(len(arr)):
            hash[arr[i]] = hash.get(arr[i] - difference, 0) + 1
            longest = max(longest, hash[arr[i]])
            # print(longest, i)
        # print()
        # hash = {}
        # for i in range(len(arr)-1,-1,-1):
        #     hash[arr[i]] = hash.get(arr[i] - difference, 0) + 1
        #     longest = max(longest, hash[arr[i]])
        #     print(longest, i)
        return longest