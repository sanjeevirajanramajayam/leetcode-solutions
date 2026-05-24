class Solution:
    def passwordStrength(self, password: str) -> int:
        score = 0
        visited = set()
        for i in password:
            if i in visited:
                continue
            if i in string.ascii_lowercase:
                score += 1
                visited.add(i)
            elif i in string.ascii_uppercase:
                score += 2
                visited.add(i)
            elif i in string.digits:
                score += 3
                visited.add(i)
            elif i in '!@#$':
                score += 5
                visited.add(i)
        return score
