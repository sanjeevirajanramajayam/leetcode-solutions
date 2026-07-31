class Solution:
    def smallestSubsequence(self, s: str) -> str:
        dic = {}
        stack = []
        for i in range(len(s)):
            dic[s[i]] = i
        visited = set()
        for i in range(len(s)):
            if s[i] in visited:
                continue
            while stack and stack[-1] > s[i] and dic[stack[-1]] > i:
                visited.remove(stack.pop())
            visited.add(s[i])
            stack.append(s[i])
            # print(stack, visited, s[i])
        return "".join(stack)