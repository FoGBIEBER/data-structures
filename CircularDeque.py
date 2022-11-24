from CircularQueue import *


class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self, item):
        self.enqueue(item)

    def deleteFront(self):
        return self.dequeue()

    def getFront(self):
        return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front -= 1
            if self.front < 0:
                self.front = MAX_QSIZE - 1

    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear -= 1
            if self.rear < 0:
                self.rear = MAX_QSIZE - 1
            return item

    def getRear(self):
        if not self.isEmpty():
            return self.items[self.rear]


# dq = CircularDeque()
# for i in range(9):  # 댁 객체 생성. f=r=0
#     if i % 2 == 0:  # i : 0, 1, 2, ... 8
#         dq.addRear(i)   # 짝수는 후단에 삽입
#     else:
#         dq.addFront(i)  # 홀수는 전단에 삽입
# dq.display()    # front=6, rear = 5
# for i in range(2):  # 전단에서 두 번의 삭제: f=8
#     dq.deleteFront()
# for i in range(3):
#     dq.deleteRear()  # 후단에서 세 번의 삭제: r=2
# dq.display()
# for i in range(9, 14):  # i : 9, 10, ... 13 : f=3
#     dq.addFront(i)
# dq.display()
