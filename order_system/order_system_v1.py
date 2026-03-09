class OrderError(Exception):
    pass

class OutOfStockError(OrderError):
    pass

class InsufficientBalanceError(OrderError):
    pass

class InvalidStateTransitionError(OrderError):
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
    
    def return_product(self) -> None:
        self._stock += 1

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
    
    def refund(self, amount: int) -> None:
        self._balance += amount
    
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

from enum import Enum, auto

class OrderStatus(Enum):
    CREATED = auto()
    PAID = auto()
    SHIPPED = auto()
    CANCELED = auto()
#Enum型は「あらかじめ決まった選択肢の中から、常に1つだけ状態をとるもの」を管理するのに使う。
#auto()は数字を割り当てる関数
#Enumのメンバーは OrderStatus型 というオリジナルの型を持っている

class OrderAction(Enum):
    PAY = auto()
    CANCEL = auto()
    SHIP = auto()

ALLOWED_TRANSITIONS = {
    OrderStatus.CREATED: {
        OrderAction.PAY: OrderStatus.PAID,
        OrderAction.CANCEL: OrderStatus.CANCELED,
    },
    OrderStatus.PAID: {
        OrderAction.SHIP: OrderStatus.SHIPPED,
        OrderAction.CANCEL: OrderStatus.CANCELED,
    },
    OrderStatus.SHIPPED: {},
    OrderStatus.CANCELED: {},
}
#次に起こり得る状態遷移を辞書で書いている（可読性が高い）

from typing import Optional
import logging
logger = logging.getLogger(__name__)    #loggerを使うための操作

class Order:
    def __init__(self, user: User, product: Product, receipt_sender: ReceiptSender, coupon: Optional[Coupon] = None):
        self._user = user
        self._product = product
        self._coupon = coupon
        self._receipt_sender = receipt_sender
        self._status = OrderStatus.CREATED
        self._paid_amount = 0
    
    @property
    def product(self):
        return self._product

    @property
    def user(self):
        return self._user

    @property
    def status(self) -> OrderStatus:
        return self._status

    #状態遷移の関数
    def _transition(self, action: OrderAction) -> None:
        allowed = ALLOWED_TRANSITIONS[self._status]

        if action not in allowed:
            raise InvalidStateTransitionError(
                f"Cannot {action.name} when status is {self._status.name}"
        )

        self._status = allowed[action]

    def pay(self):
        price = self._product.price
        if self._coupon:
            price = self._coupon.apply(price)
        
        #状態チェック
        if OrderAction.PAY not in ALLOWED_TRANSITIONS[self._status]:
            raise InvalidStateTransitionError()
        #在庫チェック
        if self._product.stock <= 0:
            raise OutOfStockError()
        
        #残高チェック
        if self._user.balance < price:
            raise InsufficientBalanceError()
        #副作用の関数内にもチェックはあるが、こっちのチェックは支払いできるかどうか、関数内のチェックは変数として成立するかのチェック

        # 副作用
        #クリティカル
        self._user.pay(price)
        self._product.decrease_stock()
        self._paid_amount = price
        #状態遷移            
        self._transition(OrderAction.PAY)
        #ノンクリティカル
        try:
             self._receipt_sender.send("Payment completed")
        except Exception as e:
            logger.error("Failed to send receipt", exc_info = e)
        #クリティカルの動作は重要度が高い、ノンクリティカルは後からでも変更できる
        #どちらも含めたトランザクションにすると、メールの不具合でも支払いに影響する

    def cancel(self):
        #状態チェック
        if OrderAction.CANCEL not in ALLOWED_TRANSITIONS[self._status]:
            raise InvalidStateTransitionError()
        
        #クリティカル副作用
        if self._status == OrderStatus.PAID:
            self._product.return_product()
            self._user.refund(self._paid_amount)
        #処理の順番は一番壊れたら困るものを最後、巻き戻しにくいものを最後、状態は事実のあととして考える
        #副作用の原子性に気を付ける（複数の処理をまとめて、全部成功するか全部失敗するかのどちらかにすること）

        self._transition(OrderAction.CANCEL)
    
    def ship(self):
        self._transition(OrderAction.SHIP)

class CheckoutService:
    def __init__(self, receipt_sender: ReceiptSender):
        self._receipt_sender = receipt_sender

    def create_order(self, user, product, coupon=None) -> Order:
        return Order(user, product, self._receipt_sender, coupon)



