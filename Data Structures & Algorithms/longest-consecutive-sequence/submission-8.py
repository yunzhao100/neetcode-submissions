class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        res=0
        for n in nums:
            if n-1 in st:
                continue
            length=1
            while n+length in nums:
                length+=1
            res=max(res,length)
        return res