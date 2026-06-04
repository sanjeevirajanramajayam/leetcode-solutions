class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        hashmap = {}
        def fn(i, j, turn):
            if i > j:
                return 0
            if (i, j, turn) in hashmap:
                return hashmap[(i, j, turn)]
            if turn == 0:
                first = piles[i] + fn(i + 1, j, 1)
                last = piles[j] + fn(i, j - 1, 1)
            else:
                first = -piles[i] + fn(i + 1, j, 0)
                last = -piles[j] + fn(i, j - 1, 0)
            # print(i, j, turn, first, last)
            hashmap[(i, j, turn)] = max(first, last)
            return max(first, last)

        dp = [[[-1 for _ in range(2)] for _ in range((len(piles) + 1))] for i in range(len(piles) + 1)]

        for i in range(len(piles)):
            for j in range(len(piles)):
                if i > j:
                    dp[i][j][0] = 0
                    dp[i][j][1] = 0

        for i in range(len(piles) - 1, -1, -1):
            for j in range(len(piles)):
                # if i > j:
                #     dp[i][j][0] = 0
                #     dp[i][j][1] = 0
                for turn in range(2):
                    if turn == 0:
                        # print(i, j)
                        first = piles[i] + dp[i + 1][j][1]
                        last = piles[j] + dp[i][j - 1][1]
                    else:
                        first = -piles[i] + dp[i + 1][j][0]
                        last = -piles[j] + dp[i][j - 1][0]
                    dp[i][j][turn] = max(first, last)
                    # print(i, j, turn, first, last)
        return True if dp[0][len(piles) - 1][0] > 0 else False