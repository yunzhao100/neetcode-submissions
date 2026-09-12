class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dic={n-1:1}
        def dp(i):
            if i in dic:
                return dic[i]
            res_len=1
            c=nums[i]
            for j in range(i+1,n):
                if nums[j]>c:
                    res_len=max(res_len,dp(j)+1)
            dic[i]=res_len
            return dic[i]
        return max(dp(i) for i in range(n))