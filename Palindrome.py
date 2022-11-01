from Stack import *


def palindrome():
    stack = Stack()
    words = str(input('회문 체크용 문자열 : '))
    for ch in words:
        if ch.isalpha():
            stack.push(ch.lower())
    output = "".join(stack.top)

    check = True
    n = stack.size() // 2

    for i in range(n):
        if stack.pop() != stack.top[i]:
            check = False
            break

    if check:
        print('{} : 회문임!!'.format(output))
    else:
        print('{} : 회문아님!!'.format(output))
