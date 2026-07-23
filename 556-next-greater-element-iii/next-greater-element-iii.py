class Solution:
    def nextGreaterElement(self, n: int) -> int:
        oldN = n
        n =  list(str(n))
        # print(n)
        i = len(n) - 1
        while i > 0 and n[i - 1] >= n[i]:
            i -= 1
        if i == 0:
            return -1
        pivot = i - 1
        j = len(n) - 1
        
        while j > 0 and n[j] <= n[pivot]:
            j -= 1

        n[j], n[pivot] = n[pivot], n[j]
        ans = int("".join(n[:i] + n[i:][::-1]))
        if (oldN == ans):
            return -1
        if ans > 2**31 - 1:
            return -1
        return ans