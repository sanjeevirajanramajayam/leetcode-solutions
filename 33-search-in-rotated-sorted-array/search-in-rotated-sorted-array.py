class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            print(nums[low:high+1])
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                # print(nums[low], nums[mid], target >= nums[low] and target <= nums[high])
                if target >= nums[low] and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:
                if target >= nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1