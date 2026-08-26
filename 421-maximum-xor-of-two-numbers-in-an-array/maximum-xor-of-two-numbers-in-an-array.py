class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}

        def insert(num):
            node = trie
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]

        def maxXOR(num):
            node = trie
            ans = ""

            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opposite = 1 - bit

                if opposite in node:
                    ans += str(opposite)
                    node = node[opposite]
                else:
                    ans += str(bit)
                    node = node[bit]
            return int(ans,2) ^ num
        
        for j in nums:
            insert(j)
        
        answer = 0

        for num in nums:
            answer = max(answer, maxXOR(num))

        return answer


        return 0