class Solution:
    def goodIndices(self, arr: List[int], k: int) -> List[int]:
        beforeGoodElements = [0 for i in range(len(arr))]
        
        afterGoodElements = [0 for i in range(len(arr))]

        for i in range(1, len(arr)):
            if arr[i - 1] >= arr[i]:
                # print(i - 1, i)
                beforeGoodElements[i] = beforeGoodElements[i - 1] + 1
            else:
                beforeGoodElements[i] = 0

        for i in range(len(arr) - 2, -1, -1):
            if arr[i + 1] >= arr[i]:
                afterGoodElements[i] = afterGoodElements[i + 1] + 1
            else:
                afterGoodElements[i] = 0
        
        # print(beforeGoodElements, afterGoodElements)
        ans = []
        for i in range(k, len(arr) - k):
            if beforeGoodElements[i - 1] >= k - 1 and afterGoodElements[i + 1] >= k - 1:
                ans.append(i)
        
        return ans