class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def nse(arr):
            stack = []
            ans = [0] * len(arr)
            for i in range(len(arr) - 1, -1, -1):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                if not stack:
                    ans[i] = len(arr)
                else:
                    ans[i] = stack[-1]
                stack.append(i)
            return ans
        
        def psee(arr):
            stack = []
            ans = [0] * len(arr)
            for i in range(len(arr)):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if not stack:
                    ans[i] = -1
                else:
                    ans[i] = stack[-1]
                stack.append(i)
            return ans

        psee = psee(arr)
        nse = nse(arr)
        count = 0
        for i in range(len(arr)):
            left = i - psee[i]
            right = nse[i] - i
            count += (left * right) * arr[i]
        return count % (10 ** 9 + 7)
