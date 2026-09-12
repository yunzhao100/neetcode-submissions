class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r # initial value is the one that definitely works
        while l<=r:
            m=(l+r)//2
            time=0
            for p in piles:
                time+=math.ceil(p/m)
            if time<=h:
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res