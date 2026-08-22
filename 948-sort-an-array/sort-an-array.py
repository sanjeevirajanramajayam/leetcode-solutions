class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, r1, l2, r2):
            # print(l1, r1, l2, r2)
            newArr = []
            i = l1
            j = l2
            while i <= r1 and j <= r2:
                if nums[i] > nums[j]:
                    newArr.append(nums[j])
                    j += 1
                else:
                    newArr.append(nums[i])
                    i += 1
            while i <= r1:
                newArr.append(nums[i])
                i += 1     
            while j <= r2:
                newArr.append(nums[j])
                j += 1
            # print(newArr)
            for i in range(len(newArr)):
                nums[i + l1] = newArr[i]
            # print(nums)

        def mergeSort(left, right):
            # print
            # print(left, right)
            if left >= right or right < left:
                return
            mid = (left + right) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            merge(left, mid, mid+1, right)
        mergeSort(0, len(nums) - 1)
        return nums