class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        prefix=[0]*len(height)
        postfix=[0]*len(height)
        for i in range(len(height)):
            prefix[i]=height[0] if i==0 else max(prefix[i-1],height[i])
        for i in range(len(height)-1,-1,-1):
            postfix[i]=height[i] if i==len(height)-1 else max(postfix[i+1],height[i])
        for i in range(len(height)):
            res+=min(prefix[i],postfix[i])-height[i]
        return res