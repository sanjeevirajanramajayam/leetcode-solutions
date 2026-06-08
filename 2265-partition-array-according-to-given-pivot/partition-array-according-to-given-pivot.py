class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        newList = []
        newList2 = []
        newList3 = []
        for i in nums:
            if i < pivot:
                newList.append(i)   
            if i == pivot:
                newList2.append(i)
            if i > pivot:
                newList3.append(i)   
        return newList + newList2 + newList3      