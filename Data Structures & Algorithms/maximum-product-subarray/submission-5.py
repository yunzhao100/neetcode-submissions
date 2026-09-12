class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmax=1
        curmin=1
        res=nums[0]
        for n in nums:
            tmp=curmax
            curmax=max(curmax*n,curmin*n,n)
            curmin=min(tmp*n,curmin*n,n)
            res=max(res,curmax)
        return res