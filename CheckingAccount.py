import BankAccount


class CheckingAccount(BankAccount.BankAccount):
    ccount = 0

    def __init__(self, name, balance, fee):
        CheckingAccount.ccount += 1
        num = "02-{0:03d}".format(CheckingAccount.ccount)
        super().__init__(name, num, balance)
        self.__fee = fee

    def check(self, amount):
        if self.getBalance() >= amount + self.__fee:
            super().withdraw(amount + self.__fee)
            return True
        else:
            return False

    def __str__(self):
        return "name : {}, number : {}, balance : {:10d}, fee : {}".format(self.getName(), self.getNum(), self.getBalance(), self.__fee)
