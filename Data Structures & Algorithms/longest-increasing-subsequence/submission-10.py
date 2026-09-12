class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        def dp(i):
            if i>=n: return 0
            if i==n-1: return 1
            if i in dic: return dic[i]
            res=1
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    res=max(res,1+dp(j))
            dic[i]=res
            return res
        return max(dp(i) for i in range(n))