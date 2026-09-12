class MinStack:

    def __init__(self):
        self.stack = []
        self.minimumStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minimumStack:
            self.minimumStack.append(val)
        elif self.minimumStack[-1] >= val:
            self.minimumStack.append(val)



    def pop(self) -> None:
        if self.top() == self.minimumStack[-1]:
            self.minimumStack.pop()
        self.stack.pop()



    def top(self) -> int:
        return self.stack[-1]


    # We need to getMin in constant time, this must be O(1)
    def getMin(self) -> int:
        return self.minimumStack[-1]
        
        