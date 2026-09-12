class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2: return max(nums)
        dic1={}
        def dp1(i):
            if i==n-2: return nums[n-2]
            if i==n-3: return max(nums[n-3],nums[n-2])
            if i in dic1: return dic1[i]
            res=max(nums[i]+dp1(i+2),dp1(i+1))
            dic1[i]=res
            return res
        dic2={}
        def dp2(i):
            if i==n-1: return nums[n-1]
            if i==n-2: return max(nums[n-2],nums[n-1])
            if i in dic2: return dic2[i]
            res=max(nums[i]+dp2(i+2),dp2(i+1))
            dic2[i]=res
            return res
        return max(dp1(0),dp2(1))