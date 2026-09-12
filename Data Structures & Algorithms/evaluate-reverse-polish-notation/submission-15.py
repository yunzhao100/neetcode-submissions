class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators={'+','-','*','/'}
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                if t=='+':
                    stack.append(stack.pop()+stack.pop())
                elif t=='-':
                    r,l=stack.pop(),stack.pop()
                    stack.append(l-r)
                elif t=='*':
                    stack.append(stack.pop()*stack.pop())
                else:
                    r,l=stack.pop(),stack.pop()
                    stack.append(int(l/r))
        return stack[0]