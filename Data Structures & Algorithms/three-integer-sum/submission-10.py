class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,n in enumerate(nums):
            if n>0:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                sm=nums[l]+n+nums[r]
                if sm==0:
                    res.append([nums[l],n,nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif sm>0:
                    r-=1
                else:
                    l+=1
        return res