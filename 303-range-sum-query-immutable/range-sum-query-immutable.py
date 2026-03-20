class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.leftSum = [0 for i in range(len(nums) + 1)]
        self.leftSum[0] = 0
        for i in range(1, len(self.leftSum)):
            self.leftSum[i] = self.leftSum[i - 1] + nums[i - 1]
        # print(self.leftSum)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # print(self.leftSum[right], self.leftSum[left])
        return self.leftSum[right + 1] - self.leftSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)