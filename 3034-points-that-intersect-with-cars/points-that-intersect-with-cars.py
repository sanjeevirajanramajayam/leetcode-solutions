class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        arr = [0] * 102
        for start, end in nums:
            arr[start] += 1
            arr[end + 1] += -1
        cnt = 0
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
            if arr[i] > 0:
                cnt += 1
        # print(arr)
        if arr[0] > 0:
            cnt += 1
        return cnt
        
