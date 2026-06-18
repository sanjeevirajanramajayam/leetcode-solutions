class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_a = (minutes * 6) % 360
        hours_a = (hour * 30) % 360
        hours_a += minutes_a / 360 * 30
        # print(minutes_a, hours_a)
        return min(abs(hours_a - minutes_a), abs( 360 - abs(minutes_a - hours_a)))