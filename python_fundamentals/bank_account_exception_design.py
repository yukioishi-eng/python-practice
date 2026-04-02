#例外設計
class InvalidTransactionError(Exception):    #エラーを細かく定義する
    pass

class InsufficientFundsError(Exception):
    pass
#こうすることで、エラーごとに別の処理をすることができる

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
            raise InvalidTransactionError("type is invalid")

    def _validate_amount(self, amount) -> None:
        if not isinstance(amount, int) or amount < 1:
            raise InvalidTransactionError("amount is invalid")


class BankAccount:
    def __init__(self, owner: str, balance: int):
        self._transactions = []
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
    def transactions(self) -> tuple[Transaction, ...]:
        return tuple(self._transactions)

    def apply_transaction(self, transaction: Transaction) -> None:
        self._validate_transaction(transaction)

        if transaction.type == "deposit":
            self._balance += transaction.amount

        elif transaction.type == "withdraw":
            if transaction.amount > self._balance:
                raise InsufficientFundsError("amount is invalid")
            self._balance -= transaction.amount

        self._transactions.append(transaction)

    def _validate_owner(self, owner) -> None:
        if not isinstance(owner, str) or owner == "":
            raise InvalidTransactionError("owner is invalid")

    def _validate_balance(self, balance) -> None:
        if not isinstance(balance, int) or balance < 0:
            raise InvalidTransactionError("balance is invalid")

    def _validate_transaction(self, transaction) -> None:
        if not isinstance(transaction, Transaction):
            raise InvalidTransactionError("transaction is invalid")
    


# 動作確認
account = BankAccount("Taro", 1000)
try:
    t3 = Transaction("withdraw", 5000)
    account.apply_transaction(t3)
except InsufficientFundsError:
    print("残高不足エラーを捕まえた")
except InvalidTransactionError:
    print("不正入力エラーを捕まえた")
