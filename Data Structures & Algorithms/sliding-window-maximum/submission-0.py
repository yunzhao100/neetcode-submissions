class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[0]*(len(nums)-k+1)
        l=0
        while l<=len(nums)-k:
            res[l]=max(nums[l:l+k])
            l+=1
        return res