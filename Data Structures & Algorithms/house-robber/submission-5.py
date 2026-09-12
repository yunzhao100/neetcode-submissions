class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        def dp(i):
            if i in dic: return dic[i]
            if i==0: return nums[0]
            if i==1: return max(nums[0],nums[1])
            dic[i]=nums[i]
            dic[i]=max(nums[i]+dp(i-2), dp(i-1))
            return dic[i]
        return dp(n-1)