class Solution:
    def isValid(self, s: str) -> bool:
        relate={')':'(', ']':'[', '}':'{'}
        stack=[]
        for _ in s:
            if _ in relate and not stack:
                return False
            elif _ in relate and stack[-1]==relate[_]:
                stack.pop()
            else:
                stack.append(_)
        return True if not stack else False