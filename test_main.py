from main import (
    User,
    Product,
    ReceiptSender,
    Order,
    OrderStatus,
    OutOfStockError,
    InsufficientBalanceError,
    InvalidStateTransitionError,
)
def test_order_initial_status_is_created():
    user = User(balance=1000)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()

    order = Order(user, product, receipt)

    assert order._status == OrderStatus.CREATED
    assert order._paid_amount == 0

def test_order_pay_success():
    user = User(balance=1000)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()

    order = Order(user, product, receipt)
    order.pay()

    assert user.balance == 500
    assert product.stock == 9
    assert order._status == OrderStatus.PAID

import pytest

def test_order_pay_insufficient_balance():
    user = User(balance=100)  # 足りない
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()

    order = Order(user, product, receipt)

    with pytest.raises(InsufficientBalanceError):
        order.pay()
    #エラー確認
    #エラー起きるべき場合の時に用いる(エラーが起きると、テストできない)

    # 副作用が起きていないことを確認
    assert user.balance == 100
    assert product.stock == 10

def test_cannot_pay_twice():
    user = User(balance=1000)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()
    order = Order(user, product, receipt)

    order.pay()

    with pytest.raises(InvalidStateTransitionError):
        order.pay()

    # 状態が変わっていないことも確認
    assert order.status == OrderStatus.PAID
    assert user.balance == 500
    assert product.stock == 9

def test_cannot_cancel_twice():
    user = User(balance=1000)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()
    order = Order(user, product, receipt)

    order.cancel()

    with pytest.raises(InvalidStateTransitionError):
        order.cancel()

    assert order.status == OrderStatus.CANCELED

def test_cannot_pay_after_cancel():
    user = User(balance=1000)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()
    order = Order(user, product, receipt)

    order.cancel()

    with pytest.raises(InvalidStateTransitionError):
        order.pay()

    assert order.status == OrderStatus.CANCELED
    assert user.balance == 1000
    assert product.stock == 10

def test_out_of_stock():
    user = User(balance=1000)
    product = Product(price=500, stock=0)
    receipt = ReceiptSender()
    order = Order(user, product, receipt)

    with pytest.raises(OutOfStockError):
        order.pay()

    assert order.status == OrderStatus.CREATED
    assert user.balance == 1000