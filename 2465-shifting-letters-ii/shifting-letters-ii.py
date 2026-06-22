class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 2)
        for start, end, direction in shifts:
            if direction == 0:
                arr[start] += -1
                arr[end+1] += 1
            else:
                arr[start] += 1
                arr[end+1] += -1
        # print(arr)

        for i in range(1, len(s) + 1):
            arr[i] += arr[i - 1]
        
        s = list(s)

        for i in range(len(s)):
            s[i] = chr(((ord(s[i]) + arr[i] - 97) % 26) + 97)
        return "".join(s)