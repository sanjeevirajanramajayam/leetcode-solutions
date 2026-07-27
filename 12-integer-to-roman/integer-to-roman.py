class Solution:
    def intToRoman(self, num: int) -> str:
        diction = {'M' : 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC':90,
        'L' : 50,
        'XL':40,
        'X':10,
        'IX':9,
        'V': 5,
        'IV':4,
        'I':1}

        list2 = list(diction.items())
        i = 0
        ans = ""
        while num > 0:
            if list2[i][1] > num:
                i += 1
            else:
                num -= list2[i][1]
                ans += list2[i][0]
        return ans