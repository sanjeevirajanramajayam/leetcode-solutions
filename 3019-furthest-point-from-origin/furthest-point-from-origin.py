class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        net_displacement = 0
        count = 0
        for i in moves:
            if i == 'L':
                net_displacement -= 1
            elif i == 'R':
                net_displacement += 1
            else:
                count += 1
        if net_displacement > 0:
            net_displacement += count
        else:
            net_displacement -= count
        return abs(net_displacement)