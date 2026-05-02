class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0
        def merge(low, mid, high, nums):
            nonlocal cnt
            left = low
            right = mid + 1
            temp = []
            while left <= mid:
                # print(left, right, nums[left:mid + 1], nums[mid+1:high + 1])
                while right <= high and nums[left] > 2 * nums[right]:
                    # print(nums[left] > 2 * nums[right])
                    right += 1
                # print(right, mid)
                cnt += right - (mid + 1)
                # print(cnt)
                left += 1
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            while left <= mid:
                temp.append(nums[left])
                left += 1
            while right <= high:
                temp.append(nums[right])
                right += 1
            # print(low, mid, high)
            for i in range(low, high + 1):
                nums[i] = temp[i-low]

        def mergeSort(low, high, nums):
            if low >= high:
                return
            mid = (low + high) // 2
            mergeSort(low, mid, nums)
            mergeSort(mid + 1, high, nums)
            merge(low, mid, high, nums)
        
        mergeSort(0, len(nums) - 1, nums)
        return cnt