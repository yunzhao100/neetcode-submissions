class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dic={}
        def dp(i,target):
            if i>=n: return 0
            if (i,target) in dic: return dic[(i,target)]
            if target !=0 and i==n-1 and (target==nums[-1] or target==-nums[-1]): return 1
            if target ==0 and i==n-1 and (target==nums[-1] or target==-nums[-1]): return 2
            res=dp(i+1,target-nums[i])+dp(i+1,target+nums[i])
            dic[(i,target)]=res
            return res
        return dp(0,target)