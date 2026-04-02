#3段の組み合わせ
from typing import Optional

def get_user(users: dict[str, dict], user_id: str) -> Optional[dict]:
    return users.get(user_id)    #.getはキーがあれば値、ないときはNoneを返す辞書専用のメソッド

def get_profile(user: dict) -> Optional[dict]:
    return user.get("profile")

def get_display_name(profile: dict) -> Optional[str]:
    return profile.get("display_name")
    

users = {
    "u001": {
        "profile": {
            "display_name": "Alice"
        }
    },
    "u002": {},
}
def get_display_name_by_id(
    users: dict[str, dict],
    user_id: str
) -> Optional[str]:
    user_info = get_user(users, user_id)
    if user_info is None:
        return None
    
    user_profile = get_profile(user_info)
    if user_profile is None:
        raise ValueError("profile does not exist")
    
    user_name = get_display_name(user_profile)  
    #変数で置いた方が関数の呼び出しが少ない
    if user_name is None:
        raise ValueError("name does not exist")
    return user_name