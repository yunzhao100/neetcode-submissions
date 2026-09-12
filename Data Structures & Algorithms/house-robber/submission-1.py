class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dic={n-1:nums[n-1],n-2:max(nums[n-2],nums[n-1])}
        def dp(i):
            # maximum profit from i to the last one
            if i in dic:
                return dic[i]
            dic[i]=max(dp(i+1),nums[i]+dp(i+2))
            return dic[i]
        return dp(0)