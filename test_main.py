from main import User, Product, ReceiptSender, Order, OrderStatus,InsufficientBalanceError

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