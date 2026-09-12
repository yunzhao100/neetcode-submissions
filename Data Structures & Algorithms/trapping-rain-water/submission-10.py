class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        Lmax,Rmax=height[l],height[r]
        res=0
        while l<r:
            Lmax=max(Lmax,height[l])
            Rmax=max(Rmax,height[r])
            if Lmax<Rmax:
                res+=max(Lmax-height[l],0)
                l+=1
            else:
                res+=max(Rmax-height[r],0)
                r-=1
        return res