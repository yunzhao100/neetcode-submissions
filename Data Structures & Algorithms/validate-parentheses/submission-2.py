class Solution:
    def isValid(self, s: str) -> bool:
        relate={'(':')', '[':']', '{':'}'}
        stack=[]
        for _ in s:
            if _ in relate:
                stack.append(_)
            elif stack and stack[-1] in relate and relate[stack[-1]]==_:
                stack.pop()
            else:
                return False
        return True if len(stack)==0 else False