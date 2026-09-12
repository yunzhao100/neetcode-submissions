class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        n=len(nums)
        for i, num in enumerate(nums):
            if i>0 and num==nums[i-1]:
                continue
            left,right=i+1,n-1
            while left<right:
                sm=nums[left]+nums[right]+num
                if sm==0:
                    res.append([num,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                elif sm>0:
                    right-=1
                else:
                    left+=1
        return res