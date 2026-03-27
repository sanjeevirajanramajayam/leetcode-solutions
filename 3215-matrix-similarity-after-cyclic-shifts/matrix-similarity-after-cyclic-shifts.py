class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        oldMat = mat[:]
        def reverse(l, r, arr):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
             
        def left_rotate(arr, k):
            n = len(arr)
            arr = arr[::-1]
            k = k % n
            reverse(0, n - k - 1, arr)
            reverse(n - k, n - 1, arr)
            return (arr)
        
        def right_rotate(arr, k):
            n = len(arr)
            arr = arr[::-1]
            k = k % n
            reverse(0, k - 1, arr)
            reverse(k, n - 1, arr)
            return (arr)
        
        for i in range(len(mat)):
            if i % 2 == 0:
                mat[i] = left_rotate(mat[i], k)
            else:
                mat[i] = right_rotate(mat[i], k)
        # print(mat, oldMat)
        return oldMat == mat