class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm%2:
            return False
        target=sm//2
        n=len(nums)
        dic={}
        def dp(i,j):
            # i到n-1，j是需要在这个范围内找到的sum
            if (i,j) in dic: return dic[(i,j)]
            if i>=n or j<0: return False
            if j==0: return True
            dic[(i,j)]=dp(i+1,j) or dp(i+1,j-nums[i]) # 不包含nums[i]或者包含
            return dic[(i,j)]
        return dp(0,target)