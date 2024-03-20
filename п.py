class InterestBearingItem:
    pass
class Asset:
    pass
class InsurableItem:
    pass


class BankAccount(Asset, InterestBearingItem, InsurableItem):
    pass
class SavingAccount(BankAccount):
    pass
class CheckingAccount(BankAccount):
    pass


class Security(Asset, InterestBearingItem ):
    pass
class Stock(Security):
    pass
class Bond(Security):
    pass


class RealEstate(Asset, InsurableItem):
    pass