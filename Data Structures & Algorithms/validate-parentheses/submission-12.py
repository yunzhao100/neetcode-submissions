class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(',']':'[','}':'{'}
        for i in s:
            if not stack and i in dic:
                return False
            if stack and i in dic and stack[-1]!=dic[i]:
                return False
            if stack and i in dic and stack[-1]==dic[i]:
                stack.pop()
            if i not in dic:
                stack.append(i)
        return True if not stack else False