class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        i = len(n) - 1
        while i > 0 and n[i] <= n[i - 1]:
            i -= 1
        if i == 0:
            return -1
        
        idx = i - 1
        # print(i, idx)
        curr = len(n) - 1
        while n[curr] <= n[idx]:
            curr -= 1
        # print(curr) 
        n[idx], n[curr] = n[curr], n[idx]
        # print(n)
        n[idx + 1:] = reversed(n[idx + 1:])
        # print(n)
        if int("".join(n)) >= 2**31:
            return -1
        return int("".join(n))