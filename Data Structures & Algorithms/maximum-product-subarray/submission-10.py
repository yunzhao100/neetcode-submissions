class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        curr_min=1
        curr_max=1
        for i,c in enumerate(nums):
            tmp=curr_max
            curr_max=max(curr_max*c,curr_min*c,c)
            curr_min=min(curr_min*c,tmp*c,c)
            res=max(res,curr_max)
        return res