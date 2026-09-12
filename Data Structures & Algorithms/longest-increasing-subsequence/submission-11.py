class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        def dp(i):
            if i<0: return 0
            if i==0: return 1
            if i in dic: return dic[i]
            res=1
            for j in range(i):
                if nums[i]>nums[j]:
                    res=max(res,dp(j)+1)
            dic[i]=res
            return res
        return max(dp(i) for i in range(n))