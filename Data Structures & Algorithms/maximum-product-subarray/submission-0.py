class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        maxpro,minpro=1,1
        for n in nums:
            if n==0:
                maxpro,minpro=1,1
            tmp=maxpro
            maxpro=max(n*maxpro,n*minpro,n)
            minpro=min(n*tmp,n*minpro,n)
            res=max(res,maxpro)
        return res