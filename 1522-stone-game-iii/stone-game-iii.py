class Solution:
    def stoneGameIII(self, piles: List[int]) -> str:
        hashmap = {}
        def fn(i, turn):
            if i >= len(piles):
                return 0
            if (i, turn) in hashmap:
                return hashmap[(i, turn)]

            if turn == 0:
                first = float('-inf')
                mid = float('-inf')
                last = float('-inf')
                first = piles[i] + fn(i + 1, 1)
                if i + 1 <= len(piles) - 1:
                    mid = (piles[i] + piles[i + 1]) + fn(i + 2, 1)
                if i + 2 <= len(piles) - 1:
                    last = (piles[i] + piles[i + 1] + piles[i + 2]) + fn(i + 3, 1)
                hashmap[(i, turn)] = max(first, last, mid)
            else:
                first = float('inf')
                mid = float('inf')
                last = float('inf')
                first = -piles[i] + fn(i + 1, 0)
                if i + 1 <= len(piles) - 1:
                    mid = -(piles[i] + piles[i + 1]) + fn(i + 2, 0)
                if i + 2 <= len(piles) - 1:
                    last = -(piles[i] + piles[i + 1] + piles[i + 2]) + fn(i + 3, 0)
            # print(i, j, turn, first, last)
                hashmap[(i, turn)] = min(first, last, mid)
            return hashmap[(i, turn)]
        val = fn(0, 0)
        if val > 0:
            return "Alice"
        elif val < 0:
            return "Bob"
        else:
            return "Tie"