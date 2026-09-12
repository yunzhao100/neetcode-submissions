class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=set(['+','-','*','/'])
        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                r,l=stack.pop(),stack.pop()
                if t=='+':
                    stack.append(r+l)
                elif t=='-':
                    stack.append(l-r)
                elif t=='*':
                    stack.append(r*l)
                elif t=='/':
                    stack.append(int(l/r))
        return stack[0]