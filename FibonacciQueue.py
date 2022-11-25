from CircularQueue import *


def fibo(n):
    q = CircularQueue()
    q.enqueue(0)
    q.enqueue(1)
    print('피보나치 수열 : ', end='')
    print(0, end=' ')
    if (n == 0):
        return
    print(1, end=' ')
    for i in range(n-1):
        q.enqueue(q.dequeue() + q.items[q.rear])
        print(q.items[q.rear], end=' ')
    return


fibo(10)  # 피보나치 수열 10개 출력
