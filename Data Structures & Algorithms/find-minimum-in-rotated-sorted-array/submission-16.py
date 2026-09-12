class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res=nums[l]
        while l<r:
            m=(l+r)//2
            if nums[r]>=nums[m]>=nums[l] or nums[r]<=nums[m]<=nums[l]:
                return min(res,min(nums[r],nums[l]))
            elif nums[m]>=nums[l]:
                res=min(res,nums[r])
                l=m+1
            else:
                res=min(res,nums[m])
                r=m-1
        return res