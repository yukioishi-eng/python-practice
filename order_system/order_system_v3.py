#ドメイン層
class OrderError(Exception):
    pass

class OutOfStockError(OrderError):
    pass

class InsufficientBalanceError(OrderError):
    pass

class InvalidStateTransitionError(OrderError):
    pass

class DomainEvent:
    pass

class OrderPaid(DomainEvent):    
    def __init__(self, order_id):
        self.order_id = order_id

from abc import ABC, abstractmethod

class OrderRepository(ABC):

    @abstractmethod
    def get(self, order_id: OrderId) -> Order:
        pass

    @abstractmethod
    def save(self, order: Order) -> None:
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


from enum import Enum, auto

class OrderStatus(Enum):
    CREATED = auto()
    PAID = auto()
    SHIPPED = auto()
    CANCELED = auto()

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

from typing import Optional
import logging
logger = logging.getLogger(__name__)

class OrderId:
    def __init__(self, value: int):
        self._validate_value(value)
        self._value = value

    @property
    def value(self) -> int:
        return self._value
    
    def __eq__(self, other):
        return isinstance(other, OrderId) and self.value == other.value
    #__eq__は == で比較したときに正しい結果を出力するためのメソッド
    #return A and BはAとBが両方当てはまるときTrueを出力する
        
    
    def _validate_value(self, value) -> None:
        if not isinstance(value, int) or value < 1:
            raise ValueError("OrderId is invalid")

class Order:
    def __init__(self, order_id: OrderId, 
    user: User, 
    product: Product, 
    coupon: Optional[Coupon] = None
    ):
        self._id = order_id
        self._user = user
        self._product = product
        self._coupon = coupon
        self._status = OrderStatus.CREATED
        self._paid_amount = 0
        self._events = []
        
    
    @property
    def product(self):
        return self._product

    @property
    def user(self):
        return self._user

    @property
    def status(self) -> OrderStatus:
        return self._status
    
    @property
    def events(self):
        return list(self._events)

    def clear_events(self):
        self._events.clear()

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
        
        if self._product.stock <= 0:
            raise OutOfStockError()
        if self._user.balance < price:
            raise InsufficientBalanceError()

        self._user.pay(price)
        self._product.decrease_stock()
        self._paid_amount = price
        self._transition(OrderAction.PAY)

        self._events.append(OrderPaid(order_id = self._id))
        

    def cancel(self):
        if OrderAction.CANCEL not in ALLOWED_TRANSITIONS[self._status]:
            raise InvalidStateTransitionError()
        
        if self._status == OrderStatus.PAID:
            self._product.return_product()
            self._user.refund(self._paid_amount)

        self._transition(OrderAction.CANCEL)
    
    def ship(self):
        self._transition(OrderAction.SHIP)


    #アプリケーション層
class ReceiptSender(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass

class CheckoutService:

    def __init__(self, order_repo: OrderRepository):
        self._order_repo = order_repo

    def create_order(self, order_id: OrderId, user, product, coupon: Optional[Coupon] = None) -> Order:

        order = Order(order_id, user, product, coupon)

        self._order_repo.save(order)

        return order

class PayOrderUseCase:

    def __init__(self, order_repo: OrderRepository, receipt_sender: ReceiptSender):
        self._order_repo = order_repo
        self._receipt_sender = receipt_sender

    def execute(self, order_id: OrderId):

        order = self._order_repo.get(order_id)

        order.pay()

        self._order_repo.save(order)

        for event in order.events:
            if isinstance(event, OrderPaid):
                self._receipt_sender.send("Payment completed")

        order.clear_events()

#インフラ層

class EmailReceiptSender(ReceiptSender):

    def send(self, message: str):
        print("send email:", message)

class SlackReceiptSender(ReceiptSender):

    def send(self, message: str):
        print("send Slack:", message)

class LINEReceiptSender(ReceiptSender):

    def send(self, message: str):
        print("send LINE:", message)

class InMemoryOrderRepository(OrderRepository):

    def __init__(self):
        self._orders = {}

    def get(self, order_id: OrderId) -> Order:
        return self._orders[order_id.value]

    def save(self, order: Order) -> None:
        self._orders[order._id.value] = order
    #リポジトリはDBへの保存・取得を隠蔽する窓口
    #今回は代わりに辞書を用いている
