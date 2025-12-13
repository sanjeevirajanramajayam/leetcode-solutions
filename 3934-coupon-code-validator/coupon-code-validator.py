class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        res = []
        for i in range(len(code)):
            if all([j.isalnum() or j == '_' for j in code[i]]) and code[i] != '':
                if businessLine[i] in ("electronics", "grocery", "pharmacy", "restaurant"):
                    if isActive[i] == True:
                        res.append((code[i], i))
        res.sort(key= lambda x: (businessLine[x[1]], x[0]))
        res = [i[0] for i in res]
        return res