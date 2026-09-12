class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for n in tokens:
            if n=='+':
                stack.append(stack.pop()+stack.pop())
            elif n=='-':
                r,l=stack.pop(),stack.pop()
                stack.append(l-r)
            elif n=='*':
                stack.append(stack.pop()*stack.pop())
            elif n=='/':
                r,l=stack.pop(),stack.pop()
                stack.append(int(l/r))
            else:
                stack.append(int(n))
        return stack[0]