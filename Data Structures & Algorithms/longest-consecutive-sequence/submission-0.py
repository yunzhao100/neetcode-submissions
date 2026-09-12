class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        start = []
        for n in nums:
            if n-1 not in st:
                start.append(n)
        
        res = 0
        for n in start:
            length = 1
            while n+length in st:
                length += 1
            res = max(res, length)
        return res