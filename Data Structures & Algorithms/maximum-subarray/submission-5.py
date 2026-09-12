class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        currmax=0
        for n in nums:
            currmax=max(currmax,0)
            currmax+=n
            res=max(res,currmax)
        return res