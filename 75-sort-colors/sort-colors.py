class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = 0
        low = 0
        high = len(arr) - 1
        while mid <= high:
            if arr[mid] == 1:
                mid += 1
            elif arr[mid] == 0:
                temp = arr[mid]
                arr[mid] = arr[low]
                arr[low] = temp
                low += 1
                mid += 1
            elif arr[mid] == 2:
                temp = arr[mid] 
                arr[mid] = arr[high]
                arr[high] = temp
                high -= 1
        