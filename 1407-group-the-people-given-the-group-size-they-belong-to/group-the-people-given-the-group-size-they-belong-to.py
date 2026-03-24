class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hash = {}
        for person in range(len(groupSizes)):
            if groupSizes[person] not in hash:
                hash[groupSizes[person]] = [[]]
            # print(len(hash[groupSizes[person]][-1]), groupSizes[person])
            if len(hash[groupSizes[person]][-1]) >= groupSizes[person]:
                hash[groupSizes[person]].append([])
            hash[groupSizes[person]][-1].append(person)
        ans = []

        for key in hash:
            ans += hash[key]
        
        return ans