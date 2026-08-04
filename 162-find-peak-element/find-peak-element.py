class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0
        
        if arr[0] > arr[1]:
            return 0
        
        if arr[len(arr) - 1] > arr[len(arr) - 2]:
            return len(arr) - 1

        left = 1
        right = len(arr) - 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] >= arr[mid + 1]:
                right = mid - 1
            elif arr[mid] <= arr[mid + 1]:
                left = mid + 1
        