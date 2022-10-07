import SavingAccount
import CheckingAccount

account = []
account.append(SavingAccount.SavingAccount('김철수', 10000, 0.05))
account.append(SavingAccount.SavingAccount('이영희', 200000, 0.03))
account.append(CheckingAccount.CheckingAccount('홍길동', 2000000, 30000))

print('통장 초기값 출력')
for i in account:
    print(i)

print('\n김철수 50000 입금, 100000 출금')
account[0].deposit(50000)
print(account[0])
if account[0].withdraw(100000):
    print(account[0])
else:
    print('잔액 부족')
    print(account[0])

print('\n이영희 100000 입금, 75000 출금')
account[1].deposit(100000)
print(account[1])
if account[1].withdraw(75000):
    print(account[1])
else:
    print('잔액 부족')
    print(account[1])

print('\n홍길동 500000 입금')
account[2].deposit(500000)
print(account[2])

print('\n이자지급 / 당좌수표 1000000 발행')
print('계산 전')
print(account[0])
print(account[1])
print(account[2])
print('계산 후')
for i in account:
    num1 = i.getNum()
    num2 = num1[0:2]
    if num2 == '01':
        i.interest()
        print(i)
    else:
        if i.check(1000000):
            print(i)
        else:
            print('잔액 부족')
            print(i)
