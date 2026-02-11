#年齢制限つきユーザー取得
users = {
    "u001": {"name": "Alice", "age": 20},
    "u002": {"name": "Bob", "age": 17},
    "u003": {"name": "Charlie", "age": 25},
}
from typing import Optional
def get_adult_user_name(
    users: dict[str, dict[str, int | str]],
    user_id: str,
    adult_age: int = 18
) -> Optional[str]:
    #user_idがないとき
    if user_id not in users:
        return None

    #"age"の項目がないまたは"age"がint型じゃないとき
    info = users[user_id]
    if "age" not in info or not isinstance(info["age"], int):      #値と型の正誤を考えるときはisinstance(値, 型)
        raise ValueError("invalid age data")

    #18歳未満の時
    if info["age"] < adult_age:
        return None

    #"name"がないとき
    if "name" not in info:
        raise ValueError("invalid name data")

    return info["name"]
