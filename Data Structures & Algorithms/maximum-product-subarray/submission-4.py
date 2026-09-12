class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxpro=1
        minpro=1
        res=nums[0]
        for n in nums:
            tmp=maxpro
            maxpro=max(maxpro*n,minpro*n,n)
            minpro=min(tmp*n,minpro*n,n)
            res=max(res,maxpro)
        return res