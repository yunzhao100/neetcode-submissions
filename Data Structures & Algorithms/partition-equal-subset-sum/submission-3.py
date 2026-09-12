class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm%2: return False
        target=sm//2
        n=len(nums)
        dic={}
        def dp(i,j):
            if (i,j) in dic: return dic[(i,j)]
            if j==0: return True
            if i>=n or j<0: return False
            res=dp(i+1,j) or dp(i+1,j-nums[i])
            dic[(i,j)]=res
            return res
        return dp(0,target)