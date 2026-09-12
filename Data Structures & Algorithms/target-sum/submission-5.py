class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dic={}
        def dp(i,target):
            if i>=n: return 0 if target!=0 else 1
            if (i,target) in dic: return dic[(i,target)]
            res=dp(i+1,target-nums[i])+dp(i+1,target+nums[i])
            dic[(i,target)]=res
            return res
        return dp(0,target)