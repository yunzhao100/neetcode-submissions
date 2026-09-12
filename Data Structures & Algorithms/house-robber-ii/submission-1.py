class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return max(nums)
        dic1={n-2:nums[n-2],n-3:max(nums[n-3],nums[n-2])}
        # the first n-1 houses
        def dp1(i):
            # from i to n-1
            if i in dic1:
                return dic1[i]
            dic1[i]=max(nums[i]+dp1(i+2),dp1(i+1))
            return dic1[i]
        dic2={n-1:nums[n-1],n-2:max(nums[n-2],nums[n-1])}
        # the last n-1 houses
        def dp2(i):
            if i in dic2:
                return dic2[i]
            dic2[i]=max(nums[i]+dp2(i+2),dp2(i+1))
            return dic2[i]
        return max(dp1(0),dp2(1))