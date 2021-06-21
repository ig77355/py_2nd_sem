class Customer:
    last_id = 0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)

class Account:
    last_id = 0
    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('new deposit updated as: ' + str(self.balance))
        else:
            print('the amount is negative')

    def charge(self, amount):
        if amount < 0:
            self.balance -= amount
            print('new deposit updated as: ' + str(self.balance))
            elif amount > self.balance:
                print('not enough money on a bank account')
        else:
            print('the amount is positive')

    def __repr__(self):
        return 'Account[{},{},{}]'.format(self.id, self.customer.lastname, self.balance)


class SavingsAccount(Account):
    interest_rate = 0.01
    def calc_interest(self):
        self.balance += self.balance*self.interest_rate

    #print(self.balance)


class CheckingAccount(Account):
    pass


c1 = Customer('John', 'Smith')
print(c1)
c2 = Customer('Anne', 'Brown')
print(c2)
a1 = SavingsAccount(c1)
a2 = CheckingAccount(c2)
print(a1)
print(a2)