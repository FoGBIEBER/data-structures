class BankAccount:
    def __init__(self, name, num, balance=0):
        self.__name = name
        self.__num = num
        self.__balance = balance

    def getName(self):
        return self.__name

    def getNum(self):
        return self.__num

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return "name : {}, balance : {}".format(self.__name, self.__balance)
