#propertyを使ったclass処理
class User:
    def __init__(self, age: int):
        self.age = age    #@pripertyがあると、この文の意味は代入ではなく、setterの呼び出しという意味になる
    

    @property
    def age(self):
        return self._age    #_をつけないと、@propertyのreturn self.ageによって、@propertyが繰り返されちゃう
    #getter(@propertyの処理)は値を読み取るときに発動する ex. print(user.age)

    @age.setter
    def age(self, value):
        self._validate_age(value)
        self._age = value
    #setterは値を代入するときに発動する ex. user.age = 4

    def _validate_age(self, age: int):
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("age is invalid")

class Product:
    def __init__(self, price: int):
        self.price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self.validate_price(value)
        self._price = value

    def validate_price(self, price):
        if price < 0:
            raise ValueError("price is invalid")

class Person:
    def __init__(self, age: int):
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self.validate(value)
        self._age = value


    def validate(self, age: int):
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("age is invalid")
        print("setter called")
p=Person(20)
p.age = 30
#__init__はp=Person(20)のようにインスタンスが作られたときに最初に動作するもの
#呼び出しや読み取りの時は直接getterやsetterが呼び出されており、__init__は動作していない


class User:
    def __init__(self, name: str, age: int, email: str):
        self.age = age
        self.name = name
        self.email = email
    
    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email
    
    @age.setter
    def age(self, value):
        self._validate_age(value)
        self._age = value

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value

    @email.setter
    def email(self, value):
        self._validate_email(value)
        self._email = value

    def _validate_age(self, age):
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("age is invalid")
    def _validate_name(self, name):
        if not isinstance(name, str) or name == "":
            raise ValueError("name is invalid")
    def _validate_email(self, email):
        if not isinstance(email, str) or email == "" or @ not in email:
            raise ValueError("email is invalid")

user = User("Taro", 20, "taro@example.com")

print(user.name)
print(user.age)
print(user.email)

user.age = 25
user.name = "Jiro"
user.email = "jiro@example.com"

print(user.name)
print(user.age)
print(user.email)
