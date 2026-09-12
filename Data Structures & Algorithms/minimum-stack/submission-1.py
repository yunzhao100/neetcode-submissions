class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini=min(self.mini,val)

    def pop(self) -> None:
        if self.stack[-1]==self.mini:
            self.stack.pop()
            self.mini=min(self.stack) if self.stack else float('inf')
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else Null

    def getMin(self) -> int:
        return self.mini if self.stack else Null
