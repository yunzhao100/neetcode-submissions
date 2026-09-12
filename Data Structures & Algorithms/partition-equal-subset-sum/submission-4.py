class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm%2: return False
        dic={}
        n=len(nums)
        def dp(i,j):
            if j==0: return True
            if j<0: return False
            if i>=n: return False
            if (i,j) in dic: return dic[(i,j)]
            res=dp(i+1,j) or dp(i+1,j-nums[i])
            dic[(i,j)]=res
            return res
        return dp(0,sm//2)