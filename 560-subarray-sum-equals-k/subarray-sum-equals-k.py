class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        hash = {0: 1}
        ans = 0
        currSum = 0
        for i in range(len(arr)):
            currSum += arr[i]
            if currSum - k in hash:
                ans += hash[currSum - k]
            hash[currSum] = hash.get(currSum, 0) + 1
        return ans
            
