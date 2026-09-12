class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm%2: return False
        target=sm//2
        dic={}
        def dp(i,j):
            # 在nums[i:]找target j
            if (i,j) in dic: return dic[(i,j)]
            if i>=len(nums) or j<0: return False
            if j==0: return True
            dic[(i,j)]=dp(i+1,j-nums[i]) or dp(i+1,j)
            return dic[(i,j)]
        return dp(0,target)