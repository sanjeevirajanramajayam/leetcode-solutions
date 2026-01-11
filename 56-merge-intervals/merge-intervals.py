class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        answers = []
        intervals = sorted(intervals, key=lambda x: x[0])
        
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if answers and start <= answers[-1][1]:
                answers[-1][1] = max(answers[-1][1], end)
            else:
                 answers.append(intervals[i])
        return answers