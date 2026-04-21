class MyQueue:

    def __init__(self):
        self.impl = []
        

    def push(self, x: int) -> None:
        self.impl.append(x)
        

    def pop(self) -> int:
        return self.impl.pop(0)
        

    def peek(self) -> int:
        return self.impl[0]
        

    def empty(self) -> bool:
        return len(self.impl) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()