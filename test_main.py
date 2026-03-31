import pytest

from main import (
    Order,
    OrderId,
    OrderPaid,
    InMemoryOrderRepository,
    InMemoryUserRepository,
    InMemoryProductRepository,
    PayOrderUseCase,
    User,
    Product,
    EventDispatcher,
    OrderPaidHandler,
    EmailReceiptSender,
    InsufficientBalanceError,
    OutOfStockError,
)

def create_dispatcher():
    dispatcher = EventDispatcher()
    handler = OrderPaidHandler(EmailReceiptSender())
    dispatcher.register(OrderPaid, handler)
    return dispatcher


def test_pay_order_insufficient_balance():
    order_repo = InMemoryOrderRepository()
    user_repo = InMemoryUserRepository()
    product_repo = InMemoryProductRepository()

    dispatcher = create_dispatcher()

    user = User(user_id=1, balance=100)
    product = Product(product_id=1, price=300, stock=10)
    order = Order(OrderId(1), user_id=1, product_id=1)

    user_repo.save(user)
    product_repo.save(product)
    order_repo.save(order)

    usecase = PayOrderUseCase(order_repo, user_repo, product_repo, dispatcher)

    with pytest.raises(InsufficientBalanceError):
        usecase.execute(OrderId(1))


def test_pay_order_out_of_stock():
    order_repo = InMemoryOrderRepository()
    user_repo = InMemoryUserRepository()
    product_repo = InMemoryProductRepository()

    dispatcher = create_dispatcher()

    user = User(user_id=1, balance=1000)
    product = Product(product_id=1, price=300, stock=0)
    order = Order(OrderId(1), user_id=1, product_id=1)

    user_repo.save(user)
    product_repo.save(product)
    order_repo.save(order)

    usecase = PayOrderUseCase(order_repo, user_repo, product_repo, dispatcher)

    with pytest.raises(OutOfStockError):
        usecase.execute(OrderId(1))


def test_order_emits_event_on_payment():
    order = Order(OrderId(1), user_id=1, product_id=1)

    order.mark_as_paid(300)

    events = order.events

    assert len(events) == 1
    assert isinstance(events[0], OrderPaid)