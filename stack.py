# 225. Implement Stack using Queues


class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# 155. Min Stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.stack += [val]
        if self.min_val:
            self.min_val += [min(val, self.min_val[-1])]
        else:
            self.min_val += [val]

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_val = self.min_val[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
print("obj.stack push 2", obj.stack)
obj.push(0)
print("obj.stack push 0", obj.stack)
obj.push(3)
print("obj.stack push 3", obj.stack)
obj.push(0)
print("obj.stack push 0", obj.stack)

param_4 = obj.getMin()
print("param_4 getMin()", param_4)
obj.pop()
print("obj.stack pop ", obj.stack)
param_6 = obj.getMin()
print("param_6 getMin()", param_6)
obj.pop()
print("obj.stack pop ", obj.stack)
# param_5 = obj.top()
print("param_8 getMin()", obj.getMin())

obj.pop()
print("obj.stack pop ", obj.stack)
print("param_9 getMin()", obj.getMin())
