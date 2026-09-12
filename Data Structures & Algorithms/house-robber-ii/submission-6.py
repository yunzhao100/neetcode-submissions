class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2: return max(nums)
        dic1={n-2:nums[-2],n-3:max(nums[-2],nums[-3])}
        def dp1(i):
            if i in dic1: return dic1[i]
            dic1[i]=max(nums[i]+dp1(i+2),dp1(i+1))
            return dic1[i]
        dic2={n-1:nums[-1],n-2:max(nums[-1],nums[-2])}
        def dp2(i):
            if i in dic2: return dic2[i]
            dic2[i]=max(nums[i]+dp2(i+2),dp2(i+1))
            return dic2[i]
        return max(dp1(0),dp2(1))