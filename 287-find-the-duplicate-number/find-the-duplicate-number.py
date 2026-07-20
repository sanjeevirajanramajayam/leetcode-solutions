class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow = 0
        # print(slow, fast)
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow