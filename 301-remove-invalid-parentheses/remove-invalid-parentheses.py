class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        res = []
        def forward(s, si, sj):
            bal = 0

            for i in range(si, len(s)):
                if s[i] == '(':
                    bal += 1
                elif s[i] == ')':
                    bal -= 1

                if bal >= 0:
                    continue
                
                for j in range(sj, i+1):
                    if s[j] == ')' and (j == sj or s[j - 1] != ')'):
                        next_s = s[:j] + s[j + 1:] 
                        forward(next_s, i, j)
            
                return 
            
            backward(s, len(s) - 1, len(s) - 1)

        def backward(s, si, sj):
            bal = 0

            for i in range(si, -1, -1):
                if s[i] == ')':
                    bal += 1
                elif s[i] == '(':
                    bal -= 1
                
                if bal >= 0:
                    continue 
                
                for j in range(sj, i - 1, -1):
                    if s[j] == '(' and (j == sj or s[j + 1] != '('):
                        new_s = s[:j] + s[j+1:]
                        backward(new_s, i - 1, j - 1)
                return 
            
            res.append(s)
        forward(s, 0, 0)
        return res
