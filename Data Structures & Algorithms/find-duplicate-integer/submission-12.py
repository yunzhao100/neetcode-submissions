class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find a meeting point in the cycle
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find the entrance to the cycle
        ptr1 = nums[0]
        ptr2 = slow
        # keep going until they meet; check first, then advance
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
