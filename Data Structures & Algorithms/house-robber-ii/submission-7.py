class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2: return max(nums)
        dic1={}
        def dp1(i):
            if i in dic1: return dic1[i]
            if i==0: return nums[0]
            if i==1: return max(nums[0],nums[1])
            dic1[i]=nums[i]
            dic1[i]=max(nums[i]+dp1(i-2),dp1(i-1))
            return dic1[i]
        dic2={}
        def dp2(i):
            if i in dic2: return dic2[i]
            if i==1: return nums[1]
            if i==2: return max(nums[1],nums[2])
            dic2[i]=nums[i]
            dic2[i]=max(nums[i]+dp2(i-2),dp2(i-1))
            return dic2[i]
        return max(dp1(n-2),dp2(n-1))