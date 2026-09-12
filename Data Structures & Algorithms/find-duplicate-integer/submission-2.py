class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0 # value 0 is not part of the cycle because the number is from 1 to n
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2=0
        while True:
            slow2=nums[slow2]
            slow=nums[slow]
            if slow2==slow:
                return slow