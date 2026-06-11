class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        target = sum(matchsticks) // 4
        sides = [0, 0, 0, 0]
        matchsticks.sort(reverse=True)
        def fn(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if fn(i + 1) == True:
                        return True
                    sides[j] -= matchsticks[i]
            return False
        
        return fn(0)