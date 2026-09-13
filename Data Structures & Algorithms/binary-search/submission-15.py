class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        i,j=0,n-1
        while i<=j:
            left,right=nums[i],nums[j]
            if left==target: return i
            if right==target: return j
            if left> target or right<target: return -1
            k=(i+j)//2
            mid=nums[k]
            if target==mid: return k
            if target<mid: j=k-1
            else: i=k+1