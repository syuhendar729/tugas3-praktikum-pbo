class BankAccount:
    def __init__(self, name, balance, currency) -> None:
        self._account_holder = name
        self._balance = balance
        self._currency = currency

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def apply_interest(self):
        self.convert('USD')
        if self._balance >= 5000:
            self._balance = self._balance + (self._balance * 0.2)
        else:
            self._balance = self._balance + (self._balance * 0.1)


    def convert(self, new_currency):
        if new_currency == 'IDR':
            if self._currency == 'USD': self._balance = self._balance * 15000
            elif self._currency == 'EUR': self._balance = self._balance * 17000
        elif new_currency == 'USD':
            if self._currency == 'IDR' and self._balance >= 15000: self._balance = self._balance / 15000
            elif self._currency == 'EUR': self._balance = self._balance * 1.09
        elif new_currency == 'EUR':
            if self._currency == 'IDR' and self._balance >= 17000: self._balance = self._balance / 17000
            elif self._currency == 'USD': self._balance = self._balance * 0.92




        

