from LinkedStack import *


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def clear(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if not self.isEmpty():
            n = self.front
            self.front = n.link
            return n.data

    def peek(self):
        if not self.isEmpty():
            return self.front.data

    def size(self):
        node = self.front
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def display(self, msg="LinkedQueue : "):
        print(msg, end='')
        node = self.front
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

# q = LinkedQueue()

# print("0~7 정수 큐에 삽입")
# for i in range(8):
#     q.enqueue(i)
# print("size: {}".format(q.size()))
# q.display()
# print()

# print("큐에서 4개 삭제")
# for i in range(4):
#     q.dequeue()
# print("size: {}".format(q.size()))
# q.display()
# print()

# print("8~13 정수 큐에 삽입")
# for i in range(8, 14):
#     q.enqueue(i)
# print("size: {}".format(q.size()))
# q.display()
# print()
