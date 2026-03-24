class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            hash[nums[i]] = i
        print(hash)
        for i in range(len(operations)):
            print(operations[i])
            oldIndex = hash[operations[i][0]]
            nums[hash[operations[i][0]]] = operations[i][1]
            hash[nums[hash[operations[i][0]]]] = oldIndex
        return nums