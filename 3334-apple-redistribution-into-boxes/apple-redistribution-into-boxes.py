class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        sumOfApples = 0
        for i in range(len(apple)):
            sumOfApples += apple[i]
        
        capacity = sorted(capacity, reverse=True)
        current_capacity = 0
        count = 0
        for i in range(len(capacity)):
            current_capacity += capacity[i]
            if current_capacity >= sumOfApples:
                return i + 1

        