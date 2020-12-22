class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.n = 0
        self.k = k
        self.queue = [None]*self.k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.n == 0:
            self.queue[self.tail] = value
            self.n += 1
            return True
        self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        self.n += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.n -= 1
            return True
        self.head = (self.head + 1) % self.k
        self.n = self.n - 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.k == self.n


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
