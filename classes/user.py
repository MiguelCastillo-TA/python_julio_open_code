class User:
    def __init__(self, balance=500):
        self.balance = balance

    def withdraw(self, amount):
        if(self.balance - amount < 0):
            print("no puede retirar dinero")
        else:
            self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def show_balance(self):
        print(f'Balanace {self.balance}')

    def transfer_money(self, other_user, amount):
        other_user.deposit(amount)
        self.withdraw(amount)
        print('Money has been transfered...')

if __name__ == '__main__':
    user1 = User()

    user2 = User(2000)

    user3 = User(5000)


    user2.transfer_money(user1, 300)

    user2.transfer_money(user3, 1000)

    user1.show_balance()
    user2.show_balance()
    user3.show_balance()




# print(user1.balance)