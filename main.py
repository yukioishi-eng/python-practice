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
#型ヒント＋docstring（読み手を意識したコード）
scores = {
    "Alice": 80,
    "Bob": 90,
    "Charlie": 90,
    "David": 50
}
def find_top_students(scores: dict[str, int], min_score: int)-> list[str]:   #引数は変数: 型 、返り値は型を書く

    #docstringはコードの表紙、概要と引数、返り値の説明を書く
    """
    Return the names of students with the highest score
    among those who meet the minimum score requirement.

    Args:
        scores (dict[str, int]): Dictionary mapping student names to scores
        min_score (int): Minimum score required to be considered

    Returns:
        list[str]: List of student names with the highest score
    """   
    passed_students = {}
    for name, score in scores.items():
        if score >= min_score:
            passed_students[name] = score
    if not passed_students:
        return []
    max_score = max(passed_students.values())  
    
    return [name for name, score in passed_students.items() if score == max_score]

#型ヒントの設定練習
def calc_total(numbers: list[int]) -> int:
    total = 0
    for n in numbers:
        total += n
    return total

def get_passed_names(scores: dict[str, int]) -> list[str]:
    """
    Return the names of students who scored 60 points or higher.

    Args:
        scores (dict[str, int]): Dictionary mapping student names to scores.

    Returns:
        list[str]: Names of students who passed.
    """
    passed_students = []
    for name, score in scores.items():
        if score >= 60:
            passed_students.append(name)

    return passed_students

#ファイル分割 ＋ import
from basics.students import get_passed_names

scores = {
    "Alice": 80,
    "Bob": 90,
    "Charlie": 55,
    "David": 40
}

passed = get_passed_names(scores)

if passed:
    print("合格者:", passed)
else:
    print("合格者なし")

from basics.students import find_top_student

top_student = find_top_student(scores)

if top_student:
    print("最高得点者:", top_student)
else:
    print("該当なし")

#if __name__ == "__main__"の使い方
import students
print("main running")
#students.pyのif __name__ == "__main__は直接実行されないと条件を満たさない
#今回はmain.pyからの実行なので、print("students loaded")は実行されない
