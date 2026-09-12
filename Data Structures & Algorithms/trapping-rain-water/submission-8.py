class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        mostL,mostR=0,0
        while l<r:
            mostL=max(mostL,height[l])
            mostR=max(mostR,height[r])
            if mostL>mostR:
                res+=mostR-height[r]
                r-=1
            else:
                res+=mostL-height[l]
                l+=1
        return res