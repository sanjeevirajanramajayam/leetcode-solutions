class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        freqMap = defaultdict(list)
        for i in range(len(nums)):
            freqMap[nums[i]].append(i)
        
        def bs(nums, target):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        
        print(freqMap)
        ans = []
        for i in queries:
            arr = freqMap[nums[i]]
            j = bs(arr, i)
            # print(j, arr, i)
            n = len(arr)
            if n == 1:
                ans.append(-1)
                continue
            left_ind = (j - 1 + n) % n
            right_ind = (j + 1) % n
            diff = float('inf')
            print(left_ind, right_ind, abs(arr[j] - arr[left_ind]), abs(arr[j] - arr[right_ind]), len(nums) -  abs(arr[j] - arr[left_ind]), len(nums) -  abs(arr[j] - arr[right_ind]))
            diff = min(diff,abs(arr[j] - arr[left_ind]), abs(arr[j] - arr[right_ind]), len(nums) -  abs(arr[j] - arr[left_ind]), len(nums) -  abs(arr[j] - arr[right_ind]))
            ans.append(diff)
        return ans

