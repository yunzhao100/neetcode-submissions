class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        res=nums[0]
        while l<=r:
            m=(l+r)//2
            if nums[l]<=nums[r]:
                return min(res,nums[l])
            if nums[m]<nums[l]:
                res=min(res,nums[m])
                r=m-1
            else:
                res=min(res,nums[r])
                l=m+1
        return res