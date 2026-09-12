class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        addition=0
        for i,n in enumerate(digits[::-1]):
            add=1 if i==0 else 0
            after=n+add+addition
            addition=0
            if after==10:
                after=0
                addition=1
            res.append(after)
        if addition:
            res.append(addition)
        return res[::-1]