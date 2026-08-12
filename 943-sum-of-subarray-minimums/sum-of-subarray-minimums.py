class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def psee(arr):
            stack = []
            psee = []
            for i in range(len(arr)):
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()
                if not stack:
                    psee.append(-1)
                else:
                    psee.append(stack[-1])
                stack.append(i)
            # print(psee)
            return psee
        def nse(arr):
            stack = []
            nse = [0] * len(arr)
            for i in range(len(arr) - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if not stack:
                    nse[i] = len(arr)
                else:
                    nse[i] = (stack[-1])
                stack.append(i)
            # print(nse)
            return nse
        nse = nse(arr)
        psee = psee(arr)
        # print(nse, psee)
        ans = 0
        for i in range(len(arr)):
            left = i - psee[i]
            right = nse[i] - i
            ans += (left * right) * arr[i]
            # print(left, right, ans, psee[i], nse[i], i)
        return ans % (10 ** 9 + 7)