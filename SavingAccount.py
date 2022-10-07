import BankAccount


class SavingAccount(BankAccount.BankAccount):
    scount = 0

    def __init__(self, name, balance, rate):
        SavingAccount.scount += 1
        num = "01-{0:03d}".format(SavingAccount.scount)
        super().__init__(name, num, balance)
        self.__rate = rate

    def interest(self):
        self.deposit(int(self.getBalance() * (self.__rate)))

    def __str__(self):
        return "name : {}, number : {}, balance : {:10d}, interest rate : {}".format(self.getName(), self.getNum(), self.getBalance(), self.__rate)
