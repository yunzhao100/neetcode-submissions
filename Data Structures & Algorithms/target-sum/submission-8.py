class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dic={}
        def dp(i,j):
            if i>=n:
                if j==0: return 1
                else: return 0
            if (i,j) in dic: return dic[(i,j)]
            res=dp(i+1,j-nums[i])+dp(i+1,j+nums[i])
            dic[(i,j)]=res
            return res
        return dp(0,target)