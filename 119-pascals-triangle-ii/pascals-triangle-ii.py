class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex + 1):
            ans.append(math.comb(rowIndex, i))
        return ans