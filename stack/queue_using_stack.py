from collections import deque

class Queue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def enq(self, x):
        self.s1.append(x)

    def deq(self):
        n = len(self.s1)
        if n == 0:
            print('queue is empty!')
            return None
        while n > 1:
            self.s2.append(self.s1.pop())
            n -= 1
        pop_ele = self.s1.pop()
        n = len(self.s2)
        while n > 0:
            self.s1.append(self.s2.pop())
            n -= 1
        return pop_ele

    def __str__(self):
        return str(self.s1)

q = Queue()
q.enq(1)
q.enq(2)
print(q)
deq_ele = q.deq()
print(deq_ele)
print(q)