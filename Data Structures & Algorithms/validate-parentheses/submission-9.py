class Solution:
    def isValid(self, s: str) -> bool:
        relate={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i not in relate:
                stack.append(i)
            elif stack and stack[-1]==relate[i]:
                stack.pop()
            else:
                return False
        return True if not stack else False