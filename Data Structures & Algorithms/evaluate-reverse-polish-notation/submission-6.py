class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators=set(['+','-','*','/'])
        stack=[]
        for i in tokens:
            if i=='+':
                stack.append(stack.pop()+stack.pop())
            elif i=='-':
                r,l=stack.pop(),stack.pop()
                stack.append(l-r)
            elif i=='*':
                stack.append(int(stack.pop())*int(stack.pop()))
            elif i=='/':
                r,l=stack.pop(),stack.pop()
                stack.append(int(l/r))
            else:
                stack.append(int(i))
        return stack[0]