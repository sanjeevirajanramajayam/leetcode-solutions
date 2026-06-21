class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq = [0] * ((10 ** 5) + 1)

        for i in range(len(costs)):
            freq[costs[i]] += 1

        cnt = 0

        for i in range(len(freq)):
            while freq[i] > 0 and coins - i >= 0:
                # print(i)
                coins -= i
                cnt += 1
                freq[i] -= 1

        return cnt