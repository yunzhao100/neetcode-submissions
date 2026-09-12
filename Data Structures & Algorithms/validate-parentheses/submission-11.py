class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(',']':'[','}':'{'}
        for i in s:
            if not stack:
                if i not in dic:
                    stack.append(i)
                else:
                    return False
            else:
                if i not in dic:
                    stack.append(i)
                elif i in dic and dic[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False