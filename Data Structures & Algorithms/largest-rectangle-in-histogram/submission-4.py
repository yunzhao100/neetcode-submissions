class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[] # (id,h)
        res=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                res=max(res,stack[-1][1]*(i-stack[-1][0]))
                start=stack[-1][0]
                stack.pop()
            stack.append((start,h))
        for i,h in stack:
            res=max(res,h*(len(heights)-i))
        return res