class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players = sorted(players, reverse=True)
        trainers = sorted(trainers, reverse=True)

        pid = 0
        tid = 0

        count = 0

        while pid < len(players):
            if players[pid] <= trainers[tid]:
                count += 1
                tid += 1
            
            if tid >= len(trainers):
                break

            pid += 1

        return count