class MyQueue:

    def __init__(self):
        self.q = []
        self.start = 0
        self.size = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        self.size += 1

    def pop(self) -> int:
        
        popped = self.q[self.start]
        self.start += 1

        return popped

    def peek(self) -> int:
        return self.q[self.start]

    def empty(self) -> bool:
        if self.start >= self.size:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()