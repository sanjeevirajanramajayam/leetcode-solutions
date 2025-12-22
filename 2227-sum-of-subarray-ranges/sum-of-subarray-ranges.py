class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def smallest(arr):
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
            return count
        def largest(arr):
            def nge(arr):
                stack = []
                ans = [0] * len(arr)
                for i in range(len(arr) - 1, -1, -1):
                    while stack and arr[stack[-1]] < arr[i]:
                        stack.pop()
                    if not stack:
                        ans[i] = len(arr)
                    else:
                        ans[i] = stack[-1]
                    stack.append(i)
                return ans
            
            def pgee(arr):
                stack = []
                ans = [0] * len(arr)
                for i in range(len(arr)):
                    while stack and arr[stack[-1]] <= arr[i]:
                        stack.pop()
                    if not stack:
                        ans[i] = -1
                    else:
                        ans[i] = stack[-1]
                    stack.append(i)
                return ans

            pgee = pgee(arr)
            nge = nge(arr)
            count = 0
            for i in range(len(arr)):
                left = i - pgee[i]
                right = nge[i] - i
                count += (left * right) * arr[i]
            return count
        return largest(nums) - smallest(nums)