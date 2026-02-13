#classの概要
    #classは型、設計図
class Dog:
    def __init__(self, name: str):    #__init__はインスタンス(設計図から作った作品　ex. dog1)が作られるときに最初に実行する処理
        self.name = name              #selfはインスタンス自身

    def bark(self) -> str:
        return f"{self.name} says woof!"

dog1 = Dog("Pochi")
print(dog1.bark())

    #Dogに年齢を追加
class Dog:
    def __init__(self, name: str, age: int):
        #nameがstr型以外または空文字のときエラー
        if not isinstance(name, str) or  name == "":    #空文字の条件がNoneだと他に0とNoneも含まれてしまう
            raise ValueError("name is invalid")
            #0<=age<=30以外またはint型でないときエラー
        if not isinstance(age, int) or age < 0 or age > 30 :    #型チェックを先にやった方が早く止められる
            raise ValueError("age is invalid")
        
        self.name = name
        self.age = age
    
    #private メソッド（クラスの内部だけで使うことを意図したメソッド）としても書ける
class Dog:
    def __init__(self, name: str, age: int):
        self._validate_name(name)
        self._validate_age(age)
        self.name = name
        self.age = age

    def _validate_name(self, name: str):
        if not isinstance(name, str) or name == "":
            raise ValueError("name is invalid")

    def _validate_age(self, age: int):
        if not isinstance(age, int) or age < 0 or age > 30:
            raise ValueError("age is invalid")
    
    #将来、ageを変更する機能を付け加えるときのためのメソッド
    def update_age(self, new_age: int):
        self._validate_age(new_age)
        self.age = new_age
        

    def introduce(self) -> str:
        return f"I am {self.name}. I am {self.age} years old."
    
    def get_life_stage(self) -> str:
        if self.age >= 3:
            return "adult"
        return "puppy"


dog2 = Dog("Pochi", 4)
print(dog2.introduce())
print(dog2.get_life_stage())