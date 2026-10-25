class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        newMonths = [0]
        temp = 0
        for i in months:
            temp += i 
            newMonths.append(temp)
        # print(newMonths)
        aam = int(arriveAlice[:2]) - 1
        aad = int(arriveAlice[3:])
        lam = int(leaveAlice[:2]) - 1
        lad = int(leaveAlice[3:])

        abm = int(arriveBob[:2]) - 1
        abd = int(arriveBob[3:])
        lbm = int(leaveBob[:2]) - 1
        lbd = int(leaveBob[3:])


        aliceDays = [i for i in range(newMonths[aam] + aad, newMonths[lam] + lad + 1 )]
        bobDays = [i for i in range(newMonths[abm] + abd, newMonths[lbm] + lbd + 1)]

        return len(set(aliceDays).intersection(set(bobDays)))