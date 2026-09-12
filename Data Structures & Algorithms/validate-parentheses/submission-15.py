class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i not in dic:
                stack.append(i)
            else:
                if stack and stack[-1]==dic[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False