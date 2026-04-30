class Solution:
    def minOperations(self, nums: list[int]) -> int:
        sieve = [1] * (100000 + 4)
        i = 2
        sieve[0] = sieve[1] = 0 
        while i * i < (100000 + 4):
            if sieve[i] != 0:        
                for j in range(i * i, len(sieve), i):
                    sieve[j] = 0
            i += 1
        cnt = 0
        for i in range(len(nums)):
            if i % 2 != 0:
                while sieve[nums[i]] == 1:
                    nums[i] += 1
                    cnt += 1
            else:
                while sieve[nums[i]] == 0:
                    nums[i] += 1
                    cnt += 1
        return cnt