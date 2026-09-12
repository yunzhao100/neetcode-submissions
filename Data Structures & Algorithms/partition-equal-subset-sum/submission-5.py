class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm%2: return False
        n=len(nums)
        dic={}
        def dp(i,target):
            if i>=n:
                if target==0: return True
                else : return False
            if (i,target) in dic: return dic[(i,target)]
            res=dp(i+1,target) or dp(i+1,target-nums[i])
            dic[(i,target)]=res
            return res
        return dp(0,sm//2)