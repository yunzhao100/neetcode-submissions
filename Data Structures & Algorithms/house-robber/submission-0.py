class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if nums[n-2]<=nums[n-1]:
            id_=n-1
        else:
            id_=n-2
        dic={n-1:(n-1,nums[n-1]), n-2:(id_,max(nums[n-2],nums[n-1]))}
        def dp(i):
            # maximum profit from i to the last
            if i in dic:
                return dic[i]
            a,b=dp(i+1)
            if a!=i+1:
                dic[i]=(i,nums[i]+b)
            else:
                # compare nums[i]+dp(i+2)[1] and dp(i+1)[1]
                if nums[i]+dp(i+2)[1]<=b:
                    dic[i]=(a,b)
                else:
                    dic[i]=(i,nums[i]+dp(i+2)[1])
            return dic[i]
        return dp(0)[1]