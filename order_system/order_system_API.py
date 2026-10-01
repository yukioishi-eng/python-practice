from order_system.order_system_v5 import (
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
    InvalidStateTransitionError,
)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#このファイルがFastAPIを実行するため、order_systemに書かない(職務分離)
from pydantic import BaseModel
class CreateOrderRequest(BaseModel):
    order_id: int
    user_id: int
    product_id: int

order_repo = InMemoryOrderRepository()
order1 = Order(OrderId(1), 1, 101)
order_repo.save(order1)

user_repo = InMemoryUserRepository()
user1 = User(user_id=1, balance=5000)
user_repo.save(user1)

product_repo = InMemoryProductRepository()
product1 = Product(product_id=101, price=1000, stock=5)
product_repo.save(product1)

dispatcher = EventDispatcher()
dispatcher.register(OrderPaid, OrderPaidHandler(EmailReceiptSender()))
pay_order_usecase = PayOrderUseCase(order_repo, user_repo, product_repo, dispatcher)



@app.get("/")
def health_check():
    return {"message": "Order API is running"}

#注文の詳細取得API
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    orderid = OrderId(order_id)
    try:
        order = order_repo.get(orderid)
        return {
            "order_id": order.id.value,
            "status": order.status.name
            #Enumのnameは状態の左辺を指定する(CREATED = auto())
        }
    except KeyError:
        raise HTTPException(status_code = 404, detail = "Order not found")

#注文の支払いAPI
@app.post("/orders/{order_id}/pay")
def pay_order(order_id: int):
    try:
        orderid = OrderId(order_id)
        pay_order_usecase.execute(orderid)
        status = order_repo.get(orderid).status.name
        #orderを受け取って、状態を確認
        return {"注文が完了しました": status}
    except KeyError:
        raise HTTPException(status_code = 404, detail="Order, User, or Product not found")

    except InsufficientBalanceError:
        raise HTTPException(status_code = 400, detail = "Insufficient user balance")

    except OutOfStockError:
        raise HTTPException(status_code = 400, detail = "Product is out of stock")

    except InvalidStateTransitionError:
        raise HTTPException(status_code = 400, detail = "Invalid order status for payment")

#Orderの作成API
@app.post("/orders")
def create_order(request: CreateOrderRequest):
    order = Order(OrderId(request.order_id), request.user_id, request.product_id)
    order_repo.save(order)
    return {"message": "Order created successfully", "order_id": order.id.value, "status": order.status.name}
