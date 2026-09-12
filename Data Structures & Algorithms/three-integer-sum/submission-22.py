class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,n in enumerate(nums):
            if n>0:
                return res
            if i>0 and n==nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                sm=n+nums[j]+nums[k]
                if sm==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                elif sm<0:
                    j+=1
                else:
                    k-=1
        return res