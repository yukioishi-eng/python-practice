#Optionalを返す関数を組み合わせる
from typing import Optional

#ユーザー情報を探す関数
def get_user(users: dict[str, dict], user_id: str) -> Optional[dict]:
    if user_id not in users:
        return None
    return users[user_id]

#名前を返す関数
def get_user_name(user: dict) -> Optional[str]:
    if "name" not in user:
        return None
    return user["name"]
#組み合わせる
def get_user_name_by_id(
    users: dict[str, dict],
    user_id: str
) -> Optional[str]:
    user = get_user(users, user_id)
    if user is None:
        return None
    
    return get_user_name(user)
