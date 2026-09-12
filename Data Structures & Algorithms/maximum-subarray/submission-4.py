class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        curr=0
        for n in nums:
            curr=n if curr<0 else curr+n
            res=max(res,curr)
        return res