class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n <=2: return max(nums)
        dic={n-1:nums[-1],n-2:max(nums[-1],nums[-2])}
        def dp(i):
            if i in dic: return dic[i]
            dic[i]=max(nums[i]+dp(i+2),dp(i+1))
            return dic[i]
        return dp(0)