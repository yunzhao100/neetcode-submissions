class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,n in enumerate(nums):
            if n>0:
                continue
            if i>0 and nums[i-1]==n:
                continue
            left,right=i+1,len(nums)-1
            while left<right:
                sm=n+nums[left]+nums[right]
                if sm==0:
                    res.append([n,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                elif sm>0:
                    right-=1
                else:
                    left+=1
        return res