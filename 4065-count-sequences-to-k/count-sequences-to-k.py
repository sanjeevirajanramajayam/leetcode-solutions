import math
from typing import List

class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        # Define a tolerance threshold for "reasonably close" numbers
        EPS = 1e-9 
        @cache
        def fn(ind, curVal):
            # print(ind, curVal)
            if ind == 0:
                cnt = 0
                # Fix: Check if curVal is close to k
                if abs(curVal - k) < EPS:
                    cnt += 1
                
                # Fix: Check if multiplied value is close to k
                if abs((curVal * nums[ind]) - k) < EPS:
                    cnt += 1
                
                # Fix: Check if divided value is close to k
                if abs((curVal / nums[ind]) - k) < EPS:
                    cnt += 1
                return cnt
            
            cnt1 = fn(ind - 1, curVal)
            cnt2 = fn(ind - 1, curVal * nums[ind])
            cnt3 = fn(ind - 1, curVal / nums[ind])
            return cnt1 + cnt2 + cnt3
        return fn(len(nums) - 1, 1)
