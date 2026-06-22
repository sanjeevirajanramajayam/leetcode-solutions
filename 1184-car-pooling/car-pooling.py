class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        arr = [0] * 1002
        
        for passenger, start, end in trips:
            if passenger > capacity:
                return False
            arr[start] += passenger
            arr[end] += -passenger
        # print(arr[:20])
        for i in range(1, len(arr)):
            # if arr[i] > capacity:
            #     return False
            arr[i] += arr[i - 1]
            if arr[i] > capacity:
                return False
        # print(arr[:20])
        return True