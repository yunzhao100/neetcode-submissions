class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        currmax=1
        currmin=1
        for n in nums:
            tmp=currmax
            currmax=max(currmax*n,currmin*n,n)
            currmin=min(tmp*n,currmin*n,n)
            res=max(res,currmax)
        return res