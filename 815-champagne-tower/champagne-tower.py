class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        glasses = [[0 for i in range(0 , j + 1)] for j in range(0, query_row + 1)]
        glasses[0][0] = poured
        # print(glasses)
        for i in range(0, query_row):
            for j in range(0, i + 1):
                quantityLeft = (glasses[i][j] - 1) / 2.0
                if quantityLeft <= 0:
                    continue
                # print(quantityLeft)
                glasses[i + 1][j] += quantityLeft
                glasses[i + 1][j + 1] += quantityLeft
        # print(glasses)
        return min(1, glasses[query_row][query_glass])