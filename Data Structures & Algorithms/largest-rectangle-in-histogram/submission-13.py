class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[] # (start,height)
        res=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                start,height=stack.pop()
                res=max(res,(i-start)*height)
            stack.append((start,h))
        for s,h in stack:
            res=max(res,(len(heights)-s)*h)
        return res