class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        low = 0
        high = len(arr) - 1
        while low <= high:
            # print(low, high)
            mid = (low + high) // 2

            if arr[mid] == target:
                return True
            if arr[mid] == arr[low] and arr[mid] == arr[high]:
                low += 1
                high -= 1
            elif arr[low] <= arr[mid]:
                # print(arr[low], arr[mid])
                if target >= arr[low] and target < arr[mid]:
                    high = mid - 1
                    # print(high)
                else:
                    low = mid + 1
            elif arr[mid] <= arr[high]:
                if target > arr[mid] and target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
         
        return False