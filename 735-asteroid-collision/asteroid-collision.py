class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack = []

        for i in range(len(a)):
            while stack and stack[-1] > 0 and a[i] < 0 and -a[i] > stack[-1]:
                stack.pop()
            if stack and a[i] < 0 and (-a[i] == stack[-1]):
                stack.pop()
                continue
            if stack and a[i] < 0 and (-a[i] < stack[-1]):
                continue
            stack.append(a[i])
        return stack