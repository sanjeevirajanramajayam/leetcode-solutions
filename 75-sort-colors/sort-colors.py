class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0000 1111 unsorted 2222

        low = 0
        high = len(arr) -1
        mid = 0

        while mid <= high:
            if arr[mid] == 1:
                mid += 1
            elif arr[mid] == 0:
                temp = arr[mid]
                arr[mid] = arr[low]
                arr[low] = temp
                mid += 1
                low += 1
            else:
                temp = arr[high]
                arr[high] = arr[mid]
                arr[mid] = temp
                high -= 1
        

                