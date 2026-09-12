class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        start=[]
        res=0
        for n in st:
            if n-1 not in st:
                start.append(n)
        for n in start:
            length=0
            while n+length in st:
                length+=1
            res=max(res,length)
        return res