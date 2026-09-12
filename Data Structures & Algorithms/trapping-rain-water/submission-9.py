class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        l,r=0,len(height)-1
        Lmax,Rmax=height[l],height[r]
        while l<r:
            Lmax=max(Lmax,height[l])
            Rmax=max(Rmax,height[r])
            if Lmax<Rmax:
                res+=Lmax-height[l]
                l+=1
            else:
                res+=Rmax-height[r]
                r-=1
        return res