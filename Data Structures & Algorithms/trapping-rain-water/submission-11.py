class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        Lmax,Rmax=height[0],height[-1]
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