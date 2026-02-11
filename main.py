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
#ユーザー検索APIのコアロジック → user_search_core.py
#年齢制限つきユーザー取得 → adult_user_optional.py

"""
2026-02-11
内容：
dict in dict の理解とアクセス方法の確認
dict.get() の挙動理解（KeyErrorとの違い）
Optional を返す関数の設計
None 伝播パターンの実装（3段チェーン）
Optional を返す関数の安全な組み合わせ
None と raise ValueError の使い分け
重複関数呼び出しを避ける設計
責務分離を意識した関数構成
"""
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