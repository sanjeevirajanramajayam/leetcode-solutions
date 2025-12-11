class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        # def upper_bound(array, target, coord):
        #     low = 0
        #     high = len(array) - 1
        #     ans = -1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if array[mid][coord] > target:
        #             ans = mid
        #             high = mid - 1
        #         else:
        #             low = mid + 1 

        # def lower_bound(array, target, coord):
        #     low = 0
        #     high = len(array) - 1
        #     ans = -1
        #     while low <= high:
        #         mid = (low + high) // 2
        #         if array[mid][coord] < target:
        #             ans = mid 
        #             low = mid + 1
        #         else:
        #             high = mid -1

        hashmapx = {}
        hashmapy = {}
        for i, j in buildings:
            if i in hashmapx:
                hashmapx[i] = [min(hashmapx[i][0], j), max(hashmapx[i][1], j)]
            else:
                hashmapx[i] = [j, j]

            if j in hashmapy:
                hashmapy[j] = (min(hashmapy[j][0], i), max(hashmapy[j][1], i))
            else:
                hashmapy[j] = [i, i]
        # print(hashmapx, hashmapy)
        count = 0
        new_build = [(3, 3)]
        for i, j in buildings:
            x_true = False
            y_true = False
            # print(i, j)
            if i in hashmapx:
                # hashmapx[i] = sorted(hashmapx[i])
                if min(hashmapx[i]) < j < max(hashmapx[i]):
                    # print(hashmapy[i][0], i, hashmapy[i][-1], "i")
                    x_true = True
            
            if j in hashmapy:
                # hashmapy[j] = sorted(hashmapy[j])
                # print(hashmapy[j])
                if min(hashmapy[j]) < i < max(hashmapy[j]):
                    # print(hashmapy[j][0], j, hashmapy[j][-1], "j")
                    y_true = True
            if x_true and y_true:
                # print(i, j)
                count += 1
        return count