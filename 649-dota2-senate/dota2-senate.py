class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D = deque([])
        R = deque([])
        for i in range(len(senate)):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while R and D:
            # print(R, D)
            if R[0] < D[0]:
                D.popleft()
                R.append(len(senate) + R.popleft())
            else:
                R.popleft()
                D.append(len(senate) + D.popleft())
            # print(R, D)
        
        if R:
            return "Radiant"
        
        if D:
            return "Dire"