#ユーザー検索APIのコアロジック
data = {
    "apple": {"price": 120, "stock": 5},
    "banana": {"price": 80, "stock": 0},
}
    #今回の辞書は：でkeyとvalueを分けている
    
    #appleの値段
price = data["apple"]["price"]
    #bananaの在庫
stock = data["banana"]["stock"]
    #"orange" が data に 存在するかどうかを if で判定
if "orange" in data:
    pass
    #banana は 存在するが、その中に "price" キーが なかった場合
if  "price" not in data["banana"]:   #not "price" ~でも動くが、"price" not in ~の方が読みやすい
    pass

print(price)
print(stock)

    #辞書から名前を探す
users = {
    "u001": {"name": "Alice", "age": 20},
    "u002": {"name": "Bob", "age": 17},
    "u003": {"name": "Charlie", "age": 25},
}


from typing  import Optional
def get_user_name(users: dict[str, dict[str, int | str]], user_id: str) -> Optional[str]:
    # 1. user_id が存在しない
    if user_id not in users:    #辞書内の要素の有無を調べるときの書き方
        return None

    user_info = users[user_id]

    # 2. name キーがない
    if "name" not in user_info:
        raise ValueError("user data has no 'name' field")

    # 3. 正常
    return user_info["name"]

print (get_user_name(users, "u001"))