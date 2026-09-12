class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[] # [start,height]
        res=0
        for i,height in enumerate(heights):
            start=i
            while stack and stack[-1][1]>height:
                s,h=stack.pop()
                start=s
                res=max(res,(i-s)*h)
            stack.append([start,height])
        for start,height in stack:
            res=max(res,(len(heights)-start)*height)
        return res