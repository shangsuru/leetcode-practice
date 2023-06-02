class MyStack:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        empty = None
        items = None
        if not self.queue1:
            empty =self.queue1
            items = self.queue2
        elif not self.queue2:
            empty = self.queue2
            items = self.queue1
        else:
            raise RuntimeError("One queue should always be empty")

        empty.append(x)
        while items:
                empty.append(items.pop(0))

    def pop(self) -> int:
        if self.queue1:
            return self.queue1.pop(0)
        return self.queue2.pop(0)

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]

        return self.queue2[0]
        

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()