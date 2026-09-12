class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        currmax=1
        currmin=1
        for n in nums:
            tmp=currmax
            currmax=max(currmax*n,currmin*n,n) # 包含当前元素的子序列的最大乘积
            currmin=min(tmp*n,currmin*n,n) # 包含当前元素的子序列的最小乘积
            res=max(res,currmax)
        return res