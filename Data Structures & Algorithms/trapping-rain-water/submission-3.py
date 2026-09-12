class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        Lmax, Rmax=height[l],height[r]
        for i,h in enumerate(height):
            Lmax=max(Lmax,height[l])
            Rmax=max(Rmax,height[r])
            if Lmax<Rmax:
                res+=Lmax-h
                l+=1
            else:
                res+=Rmax-h
                r-=1
        return res