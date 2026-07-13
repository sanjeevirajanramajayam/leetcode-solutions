class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secMap = {}
        guMap = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secMap[secret[i]] = secMap.get(secret[i], 0) + 1
        
        for i in range(len(secret)):
            if secret[i] != guess[i] and secMap.get(guess[i], -1) > 0:
                secMap[guess[i]] -= 1
                cows += 1
        return (f"{bulls}A{cows}B")