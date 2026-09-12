class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(',']':'[','}':'{'}
        for i in s:
            if i not in dic:
                stack.append(i)
            elif stack and stack[-1]==dic[i]:
                stack.pop()
            else:
                return False
        return True if not stack else False