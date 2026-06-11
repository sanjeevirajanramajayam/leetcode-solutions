class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr:
            return 0
        temp = []
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                temp.append(0)
            elif arr[i] > arr[i - 1]:
                temp.append(1)
            else:
                temp.append(-1)
        # print(temp)
        strk = 0
        start = None
        maxStrk = float('-inf')
        for i in range(len(temp)):
            # print(strk, temp[i])
            if start == None and temp[i] != -1:
                start = temp[i]
                strk +=1
                maxStrk = max(strk, maxStrk)
                continue
            if temp[i] == -1:
                strk = 0
                start = None
                continue
            if (temp[i] == 0 and start == 1) or (temp[i] == 1 and start == 0):
                start = temp[i]
                strk += 1
                maxStrk = max(strk, maxStrk)
                continue
            else:
                strk = 1
                start = temp[i]
        if maxStrk == float('-inf'):
            return 1
        return maxStrk + 1