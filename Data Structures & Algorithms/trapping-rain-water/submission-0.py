class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        postfix = [0] * n
        for i in range(n):
            prefix[i] = height[i] if i==0 else max(prefix[i-1],height[i])
        for i in range(n-1,-1,-1):
            postfix[i] = height[i] if i==n-1 else max(postfix[i+1],height[i])
        res = 0
        for i in range(n):
            res += min(prefix[i],postfix[i]) - height[i]
        return res