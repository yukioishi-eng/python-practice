#「安全な状態管理」と「不変条件の維持」
class BankAccount:
    def __init__(self, owner: str, balance: int):
        if not isinstance(owner, str) or owner =="":
            raise ValueError("owner is invalid")
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("balance is invalid")
        self._owner = owner
        self._balance = balance
    
    @property
    def owner(self) -> str:
        return self._owner
    
    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, amount: int) -> None:
        self._validate_amount(amount)
        self._balance += amount
    
    def withdraw(self, amount: int) -> None:
        self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError("amount is invalid")
        self._balance -= amount

    def _validate_amount(self, amount) -> None:
        if not isinstance(amount, int) or amount <1:
            raise ValueError("amount is invalid")

account = BankAccount("Taro", 1000)

print(account.owner)    # Taro
print(account.balance)  # 1000

account.deposit(500)

print(account.balance)  # 1500

account.withdraw(300)

print(account.balance)  # 1200
"""
account.balance = 999999
"""
    #classの複合処理
class Transaction:
    def __init__(self, type: str, amount: int):
        self._validate_type(type)
        self._validate_amount(amount)
        self._type = type
        self._amount = amount

    
    @property
    def type(self) -> str:
        return self._type
    
    @property
    def amount(self) -> int:
        return self._amount
    
    def _validate_type(self, type) -> None:
        if type != "deposit" and type != "withdraw":
            raise ValueError("type is invalid")
    def _validate_amount(self, amount) -> None:
        if not isinstance(amount, int) or amount < 1:
            raise ValueError("amount is invalid")

class BankAccount:
    def __init__(self, owner: str, balance: int):
        self._transactions = []    #Transactionクラスのインスタンスを格納するリスト
        self._validate_owner(owner)
        self._validate_balance(balance)
        self._owner = owner
        self._balance = balance
    
    @property
    def owner(self) -> str:
        return self._owner
    
    @property
    def balance(self) -> int:
        return self._balance
    
    @property
    def transactions(self) -> tuple[Transaction,...]:
        return tuple(self._transactions)    #タプルに変換して返す

    
    def apply_transaction(self, transaction: Transaction) -> None:
        self._validate_transaction(transaction)
        if transaction.type == "deposit":
            self._balance += transaction.amount
        elif transaction.type == "withdraw":
            if transaction.amount > self._balance:
                raise ValueError("amount is invalid")
            self._balance -= transaction.amount
        self._transactions.append(transaction)    #Transactionクラスのインスタンスをリストに追加
    #transactionは残金の変動を表す

    def _validate_owner(self, owner) -> None:
        if not isinstance(owner, str) or owner == "":
            raise ValueError("owner is invalid")
    def _validate_balance(self, balance) -> None:
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("balance is invalid")
    def _validate_transaction(self, transaction) -> None:
        if not isinstance(transaction, Transaction):
            raise ValueError("transaction is invalid")

account = BankAccount("Taro", 1000)

t1 = Transaction("deposit", 500)
account.apply_transaction(t1)

print(account.balance)  # 1500

t2 = Transaction("withdraw", 300)
account.apply_transaction(t2)

print(account.balance)  # 1200

print(len(account.transactions))  # 2