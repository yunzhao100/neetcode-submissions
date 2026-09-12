class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined=[[p,s] for p,s in zip(position,speed)]
        combined.sort(reverse=True)
        stack=[]
        for p,s in combined:
            t=(target-p)/s
            if stack and stack[-1]>=t:
                continue
            stack.append(t)
        return len(stack)