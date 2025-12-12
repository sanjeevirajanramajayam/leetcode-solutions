class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        events = sorted(events, key=lambda x : (int(x[1]) * -1, x[0]), reverse=True)
        count = 0
        ans = [0] * numberOfUsers
        allInc = 0
        offline = {}
        for event in events:
            if event[0] == "MESSAGE":
                if event[2] == "ALL":
                    allInc += 1
                elif event[2] == "HERE":
                    for i in range(numberOfUsers):
                        if i not in offline:
                            ans[i] += 1
                        elif int(event[1]) - offline[i] >= 60:
                            del offline[i]
                            ans[i] += 1 
                else:
                    for id in event[2].split():
                        ans[int(id[2:])] += 1
            else:
                offline[int(event[2])] = int(event[1])
        for i in range(numberOfUsers):
            ans[i] += allInc
        return (ans)
        