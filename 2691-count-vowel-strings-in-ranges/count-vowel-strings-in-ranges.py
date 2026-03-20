class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefixArray = [0 for i in range(len(words) + 1)]
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        # if words[0][0] in vowels or words[0][len(word) - 1] in vowels:
        #     prefixArray[0] += 1

        for i in range(1, len(prefixArray)):
            if words[i - 1][0] in vowels and words[i - 1][-1] in vowels:
                prefixArray[i] = prefixArray[i - 1] + 1
            else:
                prefixArray[i] = prefixArray[i - 1]
        # print(prefixArray)
        ans = []

        for left, right in queries:
            ans.append(prefixArray[right + 1] - prefixArray[left])
        return ans