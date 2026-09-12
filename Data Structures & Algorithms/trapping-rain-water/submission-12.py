class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        pre=[0]*n
        prefix=0
        for _ in range(n):
            prefix=max(prefix,height[_])
            pre[_]=prefix
        post=[0]*n
        postfix=0
        for _ in range(n-1,-1,-1):
            postfix=max(postfix,height[_])
            post[_]=postfix
        res=0
        l,r=0,n-1
        while l<=r:
            if height[l]<height[r]:
                res+=max(min(pre[l],post[l])-height[l],0)
                l+=1
            else:
                res+=max(min(pre[r],post[r])-height[r],0)
                r-=1
        return res