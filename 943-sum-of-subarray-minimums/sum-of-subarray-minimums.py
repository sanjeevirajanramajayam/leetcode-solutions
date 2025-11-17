class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def findPSEE(arr):
            stack = []
            res = [0] * len(arr)
            for i in range(len(arr)):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                if not stack:
                    res[i] = -1
                else:
                    res[i] = stack[-1]
                stack.append(i)
            return res
        def findNSE(arr):
            stack = []
            res = [0] * len(arr)
            for i in range(len(arr) - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if not stack:
                    res[i] = len(arr)
                else:
                    res[i] = stack[-1]
                stack.append(i)
            return res
        
        psee = findPSEE(arr)
        nse = findNSE(arr)
        sum = 0
        for i in range(len(arr)):
            left = i - psee[i]
            right = nse[i] - i
            sum =  (sum + ((left * right) * arr[i]) )% (10**9 + 7)
        return sum 