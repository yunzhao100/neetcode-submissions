class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r
        while l<=r:
            total=0
            m=(l+r)//2
            for p in piles:
                total+=math.ceil(p/m)
            if total>h:
                l=m+1
            elif total<=h:
                res=min(res,m)
                r=m-1
        return res