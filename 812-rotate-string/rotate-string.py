class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # print(s in 2 * s)
        if len(s) != len(goal):
            return False
        if goal in s + s:
            return True
        return False