class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,n in enumerate(nums):
            if n>0:
                return res
            if i>0 and n==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                sm=n+nums[l]+nums[r]
                if sm==0:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif sm<0:
                    l+=1
                else:
                    r-=1
        return res