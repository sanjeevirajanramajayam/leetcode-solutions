class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        def reverse(num):
            rev = 0
            while num > 0:
                rev = (rev * 10) +  num % 10
                num = num // 10
            return rev
            
        r = reverse(n)
        # print(r, n)
        sieveLen = max(r, n) + 1
        sieve = [1] * sieveLen
        sieve[0] = sieve[1] = 0
        i = 2
        # print(sieveLen, i)
        while i * i < sieveLen:
            if sieve[i] == 0:
                i += 1
                continue
            for j in range(i * i, sieveLen, i):
                sieve[j] = 0
            i += 1
            # print(i , i*i, sieveLen)
        # print(sieve)

        ansSum = 0
        for i in range(min(r, n), max(r, n) + 1):
            if sieve[i] == 1:
                ansSum += i
        return ansSum
