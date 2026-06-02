class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        s = s.strip()
        firstDigit = False
        neg = False
        zeroSeen = False
        signSeen = False
        # print(s)
        for i in range(len(s)):

            if not signSeen and not zeroSeen and not firstDigit and s[i] in ('-', '+'):
                if s[i] == '-':
                    neg = True
                signSeen = True
                continue

            if s[i] in string.digits[1:]:
                firstDigit = True
            
            if s[i] == '0':
                zeroSeen = True

            if firstDigit and s[i] in string.digits:
                ans = (ans * 10) + int(s[i])
            
            if s[i] not in string.digits:
                break
        ans = -ans if neg else ans
        if ans < -(2 ** 31):
            ans = -2 ** 31
        
        if ans > (2 ** 31 - 1):
            ans = 2 ** 31 - 1
        
        return ans