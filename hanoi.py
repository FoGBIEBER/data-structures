def hanoi_tower(n, fr, tmp, to):
    global count
    if (n == 1):
        print("원판 1: {} --> {}".format(fr, to))
        count += 1
    else:
        hanoi_tower(n - 1, fr, to, tmp)
        print("원판 {}: {} --> {}".format(n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)
        count += 1


count = 0
hanoi_tower(1, 'A', 'B', 'C')
print('총횟수 : ', count)
print('====================')
count = 0
hanoi_tower(2, 'A', 'B', 'C')
print('총횟수 : ', count)
print('====================')
count = 0
hanoi_tower(3, 'A', 'B', 'C')
print('총횟수 : ', count)
count = 0
print('====================')
hanoi_tower(4, 'A', 'B', 'C')
print('총횟수 : ', count)
print('====================')
