#実務を意識した設計演習
    #userの残金と在庫の組み合わせた購入システム
class OutOfStockError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class Product:
    def __init__(self, name: str, price: int, stock: int):
        self._validate_name(name)
        self._validate_price(price)
        self._validate_stock(stock)
        self._name = name
        self._price = price
        self._stock = stock    #setterを作らないので、直接代入

    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> int:
        return self._price
    
    @property
    def stock(self) -> int:
        return self._stock
    
    def decrease_stock(self) -> None:
        if self._stock == 0:
            raise OutOfStockError("out of stock")
        self._stock -= 1

    
    def _validate_name(self, name):
        if not isinstance(name, str) or name == "":
            raise ValueError("name is invalid")
    def _validate_price(self, price):
        if not isinstance(price, int) or price < 1:
            raise ValueError("price is invalid")
    def _validate_stock(self, stock):
        if not isinstance(stock, int) or stock < 1:
            raise ValueError("price is invalid")
    
class User:
    def __init__(self, amount: int):
        self._validate_amount(amount)
        seof._anount = amount
    
    @property
    def amount(self) -> int:
        return self._amount
    
    def withdraw(self, amount: int) -> None:
        if amount > self._amount:
            raise InsufficientBalanceError("insufficient balance")
        self._amount -= amount

    
    def _validate_amount(self, amount):
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("amount is invalid")

class PurchaseService: 
    def purchase(self, user, product) -> None:
        if product.stock == 0:
            raise OutOfStockError("out of stock")
        if user.amount < product.price:
            raise InsufficientBalanceError("insufficient balance")
        #不整合状態(片方だけ処理が実行される)を防ぐ
        product.decrease_stock()
        user.withdraw(product.price)

    #ポイント利用付き購入
class OutOfStockError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class User:
    def __init__(self, balance: int, points: int):
        self._validate_balance(balance)
        self._validate_points(points)
        self._balance = balance
        self._points = points

    @property
    def balance(self) -> int:
        return self._balance
    
    @property
    def points(self) -> int:
        return self._points
    
    def can_pay(self, amount: int) -> bool:
        return self._balance + self._points >= amount

    def pay(self, amount: int) -> None:
        if not self.can_pay(amount):
            raise InsufficientBalanceError("insufficient balance")
        if self.points >= amount:
            self._points -= amount
        else:
            paying = amount - self.points
            self.points = 0
            self._balance -= paying
    
    def _validate_balance(self, balance):
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("balance is invalid")
    def _validate_points(self, points):
        if not isinstance(points, int) or points < 0:
            raise ValueError("points is invalid")
    
class Product:
    def __init__(self, price: int, stock: int):
        self._validate_price(price)
        self.validate_stock(stock)
        self._price = price
        self._stock = stock

    @property
    def price(self) -> int:
        return self._price
    
    @property
    def stock(self) -> int:
        return self._stock
    
    def decrease_stock(self) -> None:
        if self.
        self._stock -= 1
    
    def _validate_price(self, price):
        if not isinstance(price, int) or price < 1:
            raise ValueError("price is invalid")
    def validate_stock(self, stock):
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("stock is invalid")

class PurchaseService:
    def purchase(self, user, product):
        if product.price > user.balance + user.points:
            raise InsufficientBalanceError("insufficient balance and points")
        if product.stock == 0:
            raise OutOfStockError("out of stock")
        product.decrease_stock()

        user.point_pay(product.price)
        user.pay(product.price)

"""
間違えやすい点
・__init__での代入忘れ
・self忘れ
・責務の書き忘れ