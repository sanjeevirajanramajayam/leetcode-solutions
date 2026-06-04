class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        hashmap = {}
        def fn(i, j, turn):
            if i == j:
                return piles[i] if turn == 0 else -piles[i]
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
        return True if fn(0, len(piles) - 1, 0) > 0 else False