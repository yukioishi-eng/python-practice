from main import (
    User,
    Product,
    ReceiptSender,
    Order,
    OrderStatus,
    OrderPaid,
    OutOfStockError,
    InsufficientBalanceError,
    InvalidStateTransitionError,
)

import pytest


def test_order_initial_status_is_created():

    # Arrange
    user = User(balance=1000)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()

    # Act
    order = Order(user, product, receipt)

    # Assert
    assert order.status == OrderStatus.CREATED
    assert order.paid_amount == 0
    assert order.events == []


def test_order_pay_success():

    # Arrange
    user = User(balance=1000)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()

    order = Order(user, product, receipt)

    # Act
    order.pay()

    # Assert
    assert user.balance == 500
    assert product.stock == 9
    assert order.status == OrderStatus.PAID


def test_order_paid_event_created():

    # Arrange
    user = User(balance=1000)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()

    order = Order(user, product, receipt)

    # Act
    order.pay()

    # Assert
    assert len(order.events) == 1
    assert isinstance(order.events[0], OrderPaid)


def test_order_pay_insufficient_balance():

    # Arrange
    user = User(balance=100)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()

    order = Order(user, product, receipt)

    # Act / Assert
    with pytest.raises(InsufficientBalanceError):
        order.pay()

    # 副作用なし
    assert user.balance == 100
    assert product.stock == 10


def test_cannot_pay_twice():

    # Arrange
    user = User(balance=1000)
    product = Product(price=500, stock=10)
    receipt = ReceiptSender()

    order = Order(user, product, receipt)

    order.pay()

    # Act / Assert
    with pytest.raises(InvalidStateTransitionError):
        order.pay()

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