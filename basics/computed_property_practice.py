#propertyを用いた計算プロパティ（area, full_name）を追加するクラス設計の発展練習
class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> int:
        return self._price
    #返り値を書いた方が良い
    
    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value
    
    @price.setter
    def price(self, value):
        self._validate_price(value)
        self._price = value

    def _validate_name(self, name) -> None:    #値を返さないからNone
        if not isinstance(name, str) or name == "":
            raise ValueError("name is invalid")
    def _validate_price(self, price):
        if not isinstance(price, int) or price < 0:
            raise ValueError("price is invalid")

p = Product("Apple", 120)

print(p.name)   # Apple
print(p.price)  # 120

p.price = 150   # OK

p.price = -10   # ValueError

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value):
        self._validate_width(value)
        self._width = value
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value):
        self._validate_height(value)
        self._height = value
    
    @property
    def area(self):
        return self._width * self._height
    
    def _validate_width(self, width) -> None:
        if not isinstance(width, int) or width < 1:
            raise ValueError("width is invalid")
    def _validate_height(self, height) -> None:
        if not isinstance(height, int) or height < 1:
            raise ValueError("height is invalid")

r = Rectangle(3, 4)

print(r.area)  # 12

r.width = 5

print(r.area)  # 20

class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._validate_first_name(value)
        self._first_name = value
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._validate_last_name(value)
        self._last_name = value

    @property
    def full_name(self) -> str:
        return f"{self._first_name} {self._last_name}"

    def _validate_first_name(self, name) -> None:
        if not isinstance(name, str) or name == "":
            raise ValueError("first_name is invalid")
    def _validate_last_name(self, name) -> None:
        if not isinstance(name, str) or name == "":
            raise ValueError("last_name is invalid")

user = User("Taro", "Yamada")

print(user.full_name)
# Taro Yamada

user.first_name = "Jiro"

print(user.full_name)
# Jiro Yamada