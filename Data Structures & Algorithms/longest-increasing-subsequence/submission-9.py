class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        def dp(i):
            if i in dic: return dic[i]
            if i==0: return 1
            dic[i]=1
            for j in range(i):
                if nums[j]<nums[i]:
                    dic[i]=max(dic[i],dp(j)+1)
            return dic[i]
        return max(dp(i) for i in range(n))