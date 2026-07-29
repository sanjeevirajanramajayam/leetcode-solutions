class Solution:
    def nextGreaterElement(self, n: int) -> int:
        oldN = n
        n = list(str(n))
        # print(n)
        i = len(n) - 1
        while i>0 and  n[i-1] >= n[i]:
            i -= 1
        # print(i)
        if i == 0:
            return -1 
        # print(i)  
        pivot = i - 1
        pNum = n[pivot]
        temp = len(n) - 1
        while temp >= 0 and n[temp] <= pNum:
            temp -= 1           
        # print(temp, n[temp])
        n[pivot], n[temp] = n[temp], n[pivot]

        n = n[:i] + n[i:][::-1]
        # print(n)
        if int("".join(n)) == oldN:
            return -1
        if int("".join(n)) > 2**31 - 1:
            return -1
        return int("".join(n))