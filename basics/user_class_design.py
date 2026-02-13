#classの演習
class User:
    def __init__(self, name: str, age: int, email: str):
        self._validate_name(name)
        self._validate_age(age)
        self._validate_email(email)

        self.name = name
        self.age = age
        self.email = email
    
    def _validate_name(self, name: str):
        if not isinstance(name, str) or name == "":
            raise ValueError("name is invalid")
    def _validate_age(self, age: int):
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("age is invalid")
    def _validate_email(self, email: str):
        if not isinstance(email, str) or email == "" or "@" not in email:
            raise ValueError("email is invalid")

    def update_name(self, new_name: str):
        self._validate_name(new_name)
        self.name = new_name
    def update_age(self, new_age: int):
        self._validate_age(new_age)
        self.age = new_age
    def update_email(self, new_email: str):
        self._validate_email(new_email)
        self.email = new_email