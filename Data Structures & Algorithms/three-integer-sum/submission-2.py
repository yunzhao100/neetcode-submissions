class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i>0 and n==nums[i-1]:
                continue
            left,right=i+1,len(nums)-1
            while left<right:
                sm = n+nums[left]+nums[right]
                if sm==0:
                    res.append([n,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left<right:
                        left += 1 # it is same to check if nums[right] stays same
                elif sm>0:
                    right-=1
                else:
                    left+=1
        return res