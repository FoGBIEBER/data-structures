import random


def compare_answer(ans, x):
    if ans == x:
        return 0
    elif ans < x:
        return 1
    elif ans > x:
        return -1


count = 0
n1 = int(input('시작값: '))
n2 = int(input('끝값: '))
ans = random.randint(n1, n2)

for i in range(10):
    x = int(input('숫자를 입력하세요(범위:{}~{}): '.format(n1, n2)))
    count += 1
    if compare_answer(ans, x) == 0:
        print('정답입니다. {}번 만에 맞추셨습니다.'.format(count))
        break
    elif compare_answer(ans, x) == 1:
        print('아닙니다. 더 작은 숫자입니다!')
        n2 = x - 1
    elif compare_answer(ans, x) == -1:
        print('아닙니다. 더 큰 숫자입니다!')
        n1 = x + 1
