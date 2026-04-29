class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        ans = set()
        visited = set()
        for i in range(1, int(n**(1/3) + 1)):
            for j in range(i, int(n**(1/3) + 1)):
                val = i ** 3 + j ** 3
                if val <= n:
                    if val in visited:
                        # print(i, j, val)
                        ans.add(val)
                    else:
                        visited.add(val)
        ans = list(ans)
        (ans).sort()
        return ans