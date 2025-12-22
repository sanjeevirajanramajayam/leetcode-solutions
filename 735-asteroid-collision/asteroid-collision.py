class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for i in range(len(asteroids)):
            if asteroids[i] < 0:
                while stack and -asteroids[i] > stack[-1] and stack[-1] > 0:
                    stack.pop()
                if stack and stack[-1] == -asteroids[i]:
                    stack.pop()
                    continue
                if stack and stack[-1] > -asteroids[i]:
                    continue
                stack.append(asteroids[i])
                continue
            stack.append(asteroids[i])
        return stack