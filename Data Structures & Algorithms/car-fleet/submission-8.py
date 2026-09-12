class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        combine=[[p,s] for p,s in zip(position,speed)]
        combine.sort(reverse=True)
        for p,s in combine:
            time=(target-p)/s
            if stack and time<=stack[-1]:
                continue
            stack.append(time)
        return len(stack)