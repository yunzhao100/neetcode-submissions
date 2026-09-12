class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        mostL, mostR = height[l], height[r]
        while l<r:
            mostL=max(mostL,height[l])
            mostR=max(mostR,height[r])
            if mostL<mostR:
                res+=mostL-height[l]
                l+=1
            else:
                res+=mostR-height[r]
                r-=1
        return res