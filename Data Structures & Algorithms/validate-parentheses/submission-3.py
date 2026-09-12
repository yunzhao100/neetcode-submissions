class Solution:
    def isValid(self, s: str) -> bool:
        relate={')':'(', ']':'[', '}':'{'}
        stack=[]
        for _ in s:
            if _ not in relate:
                stack.append(_)
            elif stack and stack[-1]==relate[_]:
                stack.pop()
            else:
                return False
        return True if not stack else False