class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dic={n-1:1}
        def dp(i):
            if i in dic: return dic[i]
            dic[i]=1
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    dic[i]=max(dic[i],1+dp(j))
            return dic[i]
        return max(dp(i) for i in range(n))