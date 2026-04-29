class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText
        ans = ""
        cols = int(len(encodedText)/rows)
        def go_diag(r, c):
            nonlocal ans
            while r < rows and c < cols:
                # print(r, c, rows * r + c)
                ans += encodedText[cols * r + c]
                r += 1
                c += 1 
        for i in range(cols):
            go_diag(0, i)
        return ans.rstrip()