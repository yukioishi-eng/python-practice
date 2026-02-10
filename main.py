#学習ログ

"""
2026-01-31
内容：
・if文とfor文の復習
・リストから条件に合う要素を取り出す練習
"""
# 条件に合うデータの抽出 → basics/passed_number.py

"""
2026-02-01
内容：
リストから条件（60点以上）に合う要素を処理する練習
条件を満たす要素の個数をカウントする関数を実装
不要な条件分岐を書かないシンプルな実装を意識した
"""
# 条件下での出現回数カウント → basics/count_numbers.py

"""
2026-02-03
内容：
・条件付きで最大値を求める処理を実装
・None を使って「該当なし」の状態を表現する練習
・関数の戻り値を受け取り、if文で分岐する処理を復習
・エラーを避けるために戻り値のチェックを行う重要性を理解
"""
#条件下での平均 → basics/calc_passed_avg.py
#条件下での最大値 → basics/passed_score_max.py
#Noneチェック → basics/check_none_result.py

"""
2026-02-04
内容：
・Truthy / Falsy を用いた if 文の挙動を確認
・None を明示的に判定する条件分岐を実装
・None と 空（空リスト・空文字など）を区別する処理を理解
・条件の順序を意識した if / elif / else の書き方を練習
・入力値（名前）が None または空の場合の入力チェック処理を実装
"""
#Truthy / Falsyを用いたif文 → basics/truthy_falsy_if.py
#Noneチェック関数 → basics/none_check.py
#Noneと空の区別 → basics/none_and_empty.py
#点数判定 → basics/score_judgement.py
#名前チェック関数（None または 空文字）→ basics/name_check.py

"""
2026-02-05
内容：
・for文とif文を組み合わせて、条件に合う要素を抽出する処理を実装
・条件に合う値が見つからない場合、None を返す関数を作成
・関数の戻り値を受け取り、None チェックで安全に分岐する処理を復習
"""
#最初に60以上の点数を返す関数 → first_pass_score.py

"""
2026-02-06
内容：
・辞書（名前 → 点数）を使った条件付きデータ抽出の復習
・単一結果では None、複数結果では空リスト [] を返す設計の使い分けを理解
・next(iter(dict)) を用いた初期値設定の考え方を確認
・最高得点者が複数いる場合に全員を返す処理を実装
・max() を用いた Pythonicな最大値取得方法を学習
・max(dict) / max(dict.values()) / max(dict, key=...) の違いを理解
"""
#60点以上の中で最高得点の人の名前を返す関数 → find_top_student.py
#最高得点の人が複数いる場合の処理 → find_top_students.py
#max()を用いたPythonicな処理 → find_top_students_pythonic.py

"""
2026-02-07
内容：
型ヒント（dict[str, int], list[str], str | None）の書き方を練習
docstring を用いて関数の役割・引数・戻り値を明示
フォルダ分割を行い、別ファイルの関数を import して使用
if __name__ == "__main__": を使い、実行用コードとロジックを分離
"""
#型ヒント＋docstring（読み手を意識したコード) → practice_typehint_docstring.py
#型ヒントの設定練習 → practice_typehint.py
#ファイル分割 ＋ import → run_import_students.py
#if __name__ == "__main__"の使い方 → if_main_demo.py

"""
2026-02-08
内容：
・Optional の意味と使い方を理解
返り値設計の使い分けを学習
型ヒント付き関数の実装練習
Pythonic な書き方の理解
Optional の返り値を呼び出し側で安全に扱う方法
"""
#Optional を用いた関数 → first_over_threshold_optional.py
#Optional と空リストの使い分け → students_above_threshold_list.py
#Optional と空リストの組み合わせ → top_scorers_optional_list.py

"""
2026-02-09
内容：
・Optional の意味と使いどころの理解
・raise ValueError の書き方と設計意図
・Optional と raise の使い分け判断
・型ヒントと返り値設計の整合性チェック
"""
#通常の書き方と内包表記の書き方の比較 → list_comprehension_vs_for.py
#Optional / 空リスト / 例外 のどれを返すべきか → how_to_return_values.py
#Optionalとraiseの設計判断 → optional_vs_raise_design.py

"""
2026-02-10
内容：
dict の基本構造（key: value）と dict in dict の扱い方
値と型の検証方法（isinstance）
isinstance(value, int) を用いたデータ不整合チェック
Optional と例外の設計判断（「起こりうる結果なし」→ None、「データ不整合・成立しない状態」→ raise ValueError）
年齢制限つきユーザー取得関数を設計・実装
存在チェック → データ検証 → ビジネス条件 の順で if を構成
コメントの書き方の指針（判断理由・意味 → 改行コメント、補足説明 → 横コメント）
"""
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


