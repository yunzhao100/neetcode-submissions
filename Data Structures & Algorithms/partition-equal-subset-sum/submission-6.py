class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_=sum(nums)
        if sum_%2==1: return False
        target=sum_//2
        dic={}
        def dp(i,j):
            # i: index
            # j: distance to target
            if (i,j) in dic: return dic[(i,j)]
            if j==0: return True
            if i>=len(nums): return False
            res= dp(i+1,j) or dp(i+1,j-nums[i])
            dic[(i,j)] = res
            return res
        return dp(0,target)