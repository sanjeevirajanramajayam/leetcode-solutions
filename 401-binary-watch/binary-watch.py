class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        arr = ["0"] * 10
        res = []

        def watch(ind, temp, k):

            if ind == len(temp):
                hour = int("".join(temp[:4]), 2)
                minute = int("".join(temp[4:]), 2)
                if hour > 11:
                    return
                if minute >= 60:
                    return
                if sum(map(int, temp)) == turnedOn:
                    timeString = f"{hour}:{minute:02}"
                    res.append(timeString)
                return
            if k > 0:
                temp[ind] = "1"
                watch(ind + 1, temp, k - 1)
            temp[ind] = "0"
            watch(ind + 1, temp, k)

        watch(0, arr, turnedOn)
        return res
