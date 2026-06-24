class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        sieve = [1] * (n)
        # print(sieve)
        sieve[0] = 0
        if n > 0:
            sieve[1] = 0
        
        for i in range(2, n):
            if sieve[i] == 1:
                for j in range(i * i, n, i):
                    sieve[j] = 0
        return sum(sieve)