class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def fn(i, j, left):
            
            if j == len(key):
                return 0

            if left == -1:
                return min(fn(i, j, True), fn(i, j, False))
            print(i, j, len(ring), len(key))
            if ring[i] == key[j]:
                return 1 + fn(i, j + 1, -1)

            if left:
                if i - 1 < 0:
                    return 1 + fn(i - 1 + len(ring), j, left)
                else:
                    return 1 + fn(i - 1, j, left)
            else:
                if i + 1 >= len(ring):
                    return 1 + fn(i + 1 - len(ring), j, left)
                else:
                    return 1 + fn(i + 1, j, left)
        return fn(0, 0, -1)
