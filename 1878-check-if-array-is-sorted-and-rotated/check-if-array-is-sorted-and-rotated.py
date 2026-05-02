class Solution:
    def check(self, arr: List[int]) -> bool:
        noncnt = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                noncnt += 1
        if arr[len(arr) - 1] > arr[0]:
            noncnt += 1
        if noncnt > 1:
            return False
        return True