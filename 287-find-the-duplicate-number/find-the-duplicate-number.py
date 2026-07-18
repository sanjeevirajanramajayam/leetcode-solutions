class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                slow = 0
                while fast != slow:
                    slow = nums[slow]
                    fast = nums[fast]
                    if slow == fast:
                        return slow