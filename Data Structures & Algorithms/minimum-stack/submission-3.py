class MinStack:

    def __init__(self):
        self.stack = list()
        self.minstack = list()


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minstack.append(min(self.minstack[-1] if self.minstack else val,val))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
    

    def getMin(self) -> int:
        return self.minstack[-1]
