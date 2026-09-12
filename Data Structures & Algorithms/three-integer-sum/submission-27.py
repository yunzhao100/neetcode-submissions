class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,n in enumerate(nums):
            if n>0:
                return res
            if i>len(nums)-3:
                return res
            if i>0 and n==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                sm=n+nums[l]+nums[r]
                if sm<0:
                    l+=1
                elif sm>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<=len(nums)-2 and nums[l]==nums[l-1]:
                        l+=1
                    r-=1
        return res