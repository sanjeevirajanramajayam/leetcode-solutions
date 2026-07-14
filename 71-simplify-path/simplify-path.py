class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        path = [x for x in path if x != '']
        stack = []
        for x in path:
            if x == '.':
                continue
            if x == '..' :
                if stack:
                    stack.pop()
                continue
            stack.append(x)
        return "/" + "/".join(stack)