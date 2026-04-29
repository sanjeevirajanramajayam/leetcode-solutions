class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        def count_find(num):
            nonlocal count
            while num > 0:
                if num % 10 == digit:
                    count += 1 
                num //= 10
        for i in nums:
            count_find(i)
        return count