class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        dic={}
        def dp(i,j):
            # i: index
            # j: remaining target
            if (i,j) in dic: return dic[(i,j)]
            if i>=n and j==0: return 1
            if i>=n: return 0
            res=0
            res=dp(i+1,j-nums[i])+dp(i+1,j+nums[i])
            dic[(i,j)] = res
            return res
        return dp(0,target)