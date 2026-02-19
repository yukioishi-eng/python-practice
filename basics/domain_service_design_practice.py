#テストしやすい設計
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

        if self._points >= amount:
            self._points -= amount
        else:
            remaining = amount - self._points
            self._points = 0
            self._balance -= remaining

    def _validate_balance(self, balance: int) -> None:
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("balance is invalid")

    def _validate_points(self, points: int) -> None:
        if not isinstance(points, int) or points < 0:
            raise ValueError("points is invalid")


class Product:
    def __init__(self, price: int, stock: int):
        self._validate_price(price)
        self._validate_stock(stock)
        self._price = price
        self._stock = stock

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

    def _validate_price(self, price: int) -> None:
        if not isinstance(price, int) or price < 1:
            raise ValueError("price is invalid")

    def _validate_stock(self, stock: int) -> None:
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("stock is invalid")

class Logger:
    def log(self, message: str) -> None:
        print(message)

class PurchaseService:
    def __init__(self, logger: Logger):
        self._logger = logger
    #loggerを外部から受け取る

    def purchase(self, user: User, product: Product) -> None:
        if not user.can_pay(product.price):
            raise InsufficientBalanceError("insufficient balance")

        product.decrease_stock()
        user.pay(product.price)
        self._logger.log(f"User purchased product for {product.price}")


    #メール通知付き注文キャンセル
class CancelCompletedError(Exception):
    pass

class Order:
    def __init__(self, price: int, is_canceled: bool):
        self._validate_price(price)
        self._validate_is_canceled(is_canceled)
        self._price = price
        self._is_canceled = is_canceled
    
    @property
    def price(self) -> int:
        return self._price

    @property
    def is_canceled(self) -> bool:
        return self._is_canceled
    
    def cancel(self) -> None:
        if self._is_canceled:
            raise CancelCompletedError("cancellation has been made")
        self._is_canceled = True
    
    def _validate_price(self, price) -> None:
        if not isinstance(price, int) or price < 1:
            raise ValueError("price is invalid")
    def _validate_is_canceled(self, is_canceled) -> None:
        if not isinstance(is_canceled, bool) :
            raise ValueError("is_canceled is invalid")

class User:
    def __init__(self, balance: int):
        self._validate_balance(balance)
        self._balance = balance
    
    @property
    def balance(self) -> int:
        return self._balance
    
    def pay(self, price: int) -> None:
        self._balance += price
    
    def _validate_balance(self, balance) -> None:
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("balance is invalid")

class Notifier:
    def notify(self, message: str) -> None:
        self._validate_message(message)
        print(message)
    
    def _validate_message(self, message) -> None:
        if not isinstance(message, str) or message == "":
            raise ValueError("message is invalid")


class CancelService:
    def __init__(self, notifier: Notifier):
        self._notifier = notifier

    def cancel(self, user: User, order: Order):
        order.cancel()
        user.pay(order.price)
        self._notifier.notify("cancellation is made")

    #クーポン適用付き注文確定
class OutOfStockError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class Product:
    def __init__(self, price: int, stock: int):
        self._validate_price(price)
        self._validate_stock(stock)
        self._price = price
        self._stock = stock

    @property
    def price(self) -> int:
        return self._price
    
    @property
    def stock(self) -> int:
        return self._stock
    
    def decrease_stock(self) -> None:
        if self._stock == 0:
            raise OutOfStockError("Out of stock")
        self._stock -= 1

    def _validate_price(self, price):
        if not isinstance(price, int) or price < 1:
            raise ValueError("price is invalid")
    def _validate_stock(self, stock):
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("stock is invalid")

class User:
    def __init__(self, balance: int):
        self._validate_balance(balance)
        self._balance = balance
    
    @property
    def balance(self) -> int:
        return self._balance
    
    def pay(self, amount: int) -> None:
        if self._balance < amount:
            raise InsufficientBalanceError("insufficient balance")
        self._balance -= amount
    
    def _validate_balance(self, balance) -> None:
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("balance is invalid")

class Coupon:
    def __init__(self, discount_amount: int):
        self._validate_discount_amount(discount_amount)
        self._discount_amount = discount_amount
    
    @property
    def discount_amount(self) -> int:
        return self._discount_amount

    def apply(self, price) -> int:
        if self._discount_amount > price:
            raise ValueError("price or discount_amount is invalid")
        return price - self._discount_amount
    
    def _validate_discount_amount(self, discount_amount) -> None:
        if not isinstance(discount_amount, int) or discount_amount < 1:
            raise ValueError("discount_amount is invalid")

class ReceiptSender:
    def send(self, message: str) -> None:
        print(message)

class CheckoutService:
    def __init__(self, receipt_sender: ReceiptSender):
        self._receipt_sender = receipt_sender

    def checkout(self, user: User, product: Product, coupon: Coupon):
        discounted_price = coupon.apply(product.price)
        user.pay(discounted_price)
        product.decrease_stock()
       
        self._receipt_sender.send("Payment has been completed")
    #不整合状態になる可能性があるので、順番には気を付ける

