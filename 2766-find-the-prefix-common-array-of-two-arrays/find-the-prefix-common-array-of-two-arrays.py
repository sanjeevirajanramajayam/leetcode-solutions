class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set1 = set()
        set2 = set()
        ans = []
        for j in range(len(A)):
            set1.add(A[j])
            set2.add(B[j])
            ans.append(len(set1.intersection(set2)))
        return ans