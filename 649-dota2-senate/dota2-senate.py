class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque([])
        D = deque([])
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)

        while R and D:
            r = R.popleft()
            d = D.popleft()
            if (r > d):
                D.append(d + n)
            else:
                R.append(r + n)
        
        if not R:
            return "Dire"
        
        if not D:
            return "Radiant"
