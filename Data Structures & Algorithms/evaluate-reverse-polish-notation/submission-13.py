class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = set(['+','-','*','/'])
        stack=[]
        for t in tokens:
            if t not in op:
                stack.append(int(t))
            else:
                right,left=stack.pop(),stack.pop()
                if t=='+':
                    stack.append(left+right)
                elif t=='-':
                    stack.append(left-right)
                elif t=='*':
                    stack.append(left*right)
                else:
                    stack.append(int(left/right))
        return stack[0]