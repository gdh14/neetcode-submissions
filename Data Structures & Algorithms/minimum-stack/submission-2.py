"""
Idea: Instead of searching the whole stack to find the minimum every time, we can keep a second stack that always stores the minimum value up to that point.

Example:

stack = [4,1,2]
min_stack = [4,1,1]

m = MinStack()
m.push(4)
m.push(1)
m.push(2)

"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
            return
        
        # new value is smaller
        if self.min_stack[-1] > val:
            self.min_stack.append(val)
        # old value is smaller 
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
