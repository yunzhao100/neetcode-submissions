class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[] # (start,height)
        res=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                start,height=stack.pop()
                res=max(res,height*(i-start))
            stack.append((start,h))
        for start,height in stack:
            res=max(res,height*(len(heights)-start))
        return res