class Solution:
    def rob(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)
        def dp(i):
            if i==n-1: return nums[-1]
            if i==n-2: return max(nums[-1],nums[-2])
            if i in dic: return dic[i]
            res=max(nums[i]+dp(i+2),dp(i+1))
            dic[i]=res
            return res
        return dp(0)