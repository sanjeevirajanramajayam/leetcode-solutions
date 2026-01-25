class Solution(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def rotateArray(arr, k):
            k = k % len(arr)
            newArr = [0] * len(arr)
            temp = []
            for i in range(k):
                temp.append(arr[i])
            
            for i in range(len(arr) - k):
                newArr[i] = arr[i + k]
            
            j = 0
            for i in range(len(arr) - k, len(arr)):
                newArr[i] = temp[j]
                j += 1
            return newArr
        # print(rotateArray([1, 3], k = 3))
        negArray = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                negArray.append(i)
                
        if not negArray:
            return nums
        indexMap = {}
        newNegArray = rotateArray(negArray, k)
        # print(negArray, newNegArray)
        for i in range(len(negArray)):
            indexMap[negArray[i]] = newNegArray[i]
        # print(indexMap)
        res = []
        for i in range(len(nums)):
            if i in indexMap:
                res.append(nums[indexMap[i]])
            else:
                res.append(nums[i])
        # print(res)
        return res 