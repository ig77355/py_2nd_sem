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
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print('New deposit updated as: ' + str(self._balance))
        else:
            raise BankException('The amount is negative')

    def charge(self, amount):
        if amount > self._balance:
            raise NotEnoughBalanceException(
                "You don't have enough Balance. Your Current Balance is " + str(self._balance))
        if amount <= 0:
            raise NegativeAmountException("The amount is negative. Please input the positive amount")
        else:
            self._balance -= amount
            print("Charge amount is: " + str(amount))
            print("New Balance updated as: " + str(self._balance))

    # def __repr__(self):
    #   return 'Account[{},{},{}]'.format(self.id, self.customer.lastname, self._balance)

    # Adding information whether it's savings or checking account
    def __repr__(self):
        return "{0}[{1},{2},{3},{4}]".format(self.__class__.__name__, self.id, self._balance,
                                             self.customer.lastname, self.customer.firstname)


class SavingsAccount(Account):
    interest_rate = 0.01

    def calc_interest(self):
        self._balance += self.interest_rate * self._balance


class CheckingAccount(Account):
    pass


class BankException(Exception):
    pass


class NegativeAmountException(BankException):
    pass


class NotEnoughBalanceException(BankException):
    pass


class Bank:
    def __init__(self):
        self.accounts = []
        self.customers = []

    def new_customer(self, first_name, last_name):
        c = Customer(first_name, last_name)
        self.customers.append(c)
        return c

    def create_account(self, customer):
        a = Account(customer)
        self.accounts.append(a)
        return a

    def transfer(self, acc_from, acc_to, amount):
        acc_from.charge(amount)
        acc_to.deposit(amount)
        pass

    def __str__(self):
        return 'Bank[{0}, {1}]'.format(self.customers, self.accounts)


c1 = Customer('John', 'Smith')
# print(c1)
c2 = Customer('Anne', 'Brown')
# print(c2)
c3 = Customer('Namjoon', 'Kim')
# print(c3)
del c2
c2 = Customer('Anne2', 'Brown')
# print(c2)
a1 = SavingsAccount(c1)
a2 = CheckingAccount(c2)
a3 = CheckingAccount(c3)
print(a1)
a1.deposit(100)
a2.deposit(200)
a3.deposit(613)
a1.calc_interest()

Bank.transfer()

try:
    a1.charge(100)
    a1.calc_interest()
    a1.charge(700)
    print('After charging')
    print(a1)
except NotEnoughBalanceException as nebe:
    print('Exception: ' + str(nebe))
except BankException as nebe:
    # except BankException as nebe:
    print('General Exception: ' + str(nebe))
# except NegativeAmountException as nae:
#     print('Exception: ' + str(nae))
print('running further')
print('----List of clients w/ accounts and balance----')
print(a1)
print(a2)
print(a3)

'''
class Bank(Account):
    # Customer Factory

    def __init__(self, customer):
        super().__init__(Customer)
        self.last_name = None
        self.first_name = None

    def new_customer(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        c = Customer(self.first_name, self.last_name)
        Account.last_id += 1
        Customer.List = [c]
        Customer.List.append['Jungkook', 'Jeon']
        return "{0}[{1},{2},{3}]".format(self.__class__.__name__, Account.last_id,
                                         self.last_name, self.first_name)

        # TODO add customer to a list

    # Add account factory to bank

    # Implement transfer
    def transfer(self, from_acc_id, to_acc_id):
        t = Transfer(self.from_acc_id, self.to_acc_id)
        amount = Account.charge(f)
        amount = Account.deposit(t, amount)
        # TODO implement
        pass
'''