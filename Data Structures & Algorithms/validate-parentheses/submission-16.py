class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={'}':'{',']':'[',')':'('}
        for i in s:
            if i in dic and (not stack or stack[-1]!=dic[i]):
                return False
            elif i in dic and stack[-1]==dic[i]:
                stack.pop()
            else:
                stack.append(i)
        return True if not stack else False