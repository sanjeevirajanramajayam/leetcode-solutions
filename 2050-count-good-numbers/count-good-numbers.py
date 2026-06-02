class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # def fn(x):
        #     if x == n:
        #         return 1
        #     if x % 2 == 0:
        #         return 5 * fn(x + 1)
        #     else:
        #         return 4 * fn(x + 1)

        # return fn(0) % (10 ** 9 + 7)
        def pow(x, n):
            if n == 0:
                return 1

            if n % 2 == 0:
                return pow((x * x) % (10 ** 9 + 7), n // 2)
            else:
                return (x * pow((x * x) % (10 ** 9 + 7), n // 2) % (10 ** 9 + 7))
        return (pow(5, (ceil(n / 2))) * pow(4, (n // 2))) % (10 ** 9 + 7)