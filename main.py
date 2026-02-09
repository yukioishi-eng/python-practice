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
#通常の書き方と内包表記の書き方の比較
def passed_students_for(scores: dict[str, int], min_score: int) -> list[str]:
    """
    Return a list of student names with scores >= min_score.
    """
    passed_students = []
    for name, score in scores.items():
        if score >= min_score:
            passed_students.append(name)
    return passed_students

def passed_students_pythonic(scores: dict[str, int], min_score: int) -> list[str]:
    """
    Return a list of student names with scores >= min_score.
    """
    return [name for name, score in scores.items() if score >= min_score]

    """
    内包表記を選ぶとき ✅
    ・条件が1つ（or とても単純）
    ・集めるだけ（append 以外の処理がない）
    ・1行で意味が崩れない
    ・「一覧を作る」処理
     → 今回のケースは合っている

    for ループを選ぶとき ✅
    ・条件が複雑・分岐が多い
    ・途中でログ・print・例外処理を入れたい
    ・今後仕様変更が入りそう
    ・読み手が初学者寄り
    """

#Optional / 空リスト / 例外 のどれを返すべきか
    #合格点以上の生徒名リストを返す
def passed_students(scores: dict[str, int], passing: int) -> list[str]:
    """
    Return a list of student names with scores >= passing.
    """
    return [name for name, score in scores.items() if score >= passing]
    """
    「合格者がいない」は異常ではない
    Optional にすると None チェックが増えて逆に面倒
    よって、空リストで返すのが正解
    """

    #条件を満たすトップスコアの生徒1人を探す
from typing import Optional

def top_student(scores: dict[str, int], passing: int) -> Optional[str]:
    """
    Return the name of the student with the highest score >= passing.
    Return None if no student meets the condition.
    """
    passed_students = {name: score for name, score in scores.items() if score >= passing}

    if not passed_students:
        return None

    max_score = max(passed_students.values())

    for name, score in passed_students.items():
        if score == max_score:
            return name
    """
    条件に合う人が必ずいるとは限らない
    Noneを返す選択肢もある
    よって、Optionalにするのが正解
    """

    #点数データが空の場合
def average_score(scores: dict[str, int]) -> float:
    """
    Return the average score.
    Raise ValueError if scores is empty.
    """
    if not scores:
        raise ValueError("scores is empty")
    #raiseは処理を終了させてエラーとして返す
    #raise エラー内容("エラーメッセージ")と書く 

    total = 0
    cnt = 0
    for score in scores.values():
        total += score
        cnt += 1

    return total / cnt

def average_score(scores: dict[str, int]) -> float:
    if not scores:
        raise ValueError("scores is empty")
    return sum(scores.values()) / len(scores)
    #合計はsumを使ってpythonicに

#Optionalとraiseの設計判断
def max_score(scores: dict[str, int]) -> int:
    """
    Return the maximum score.
    Raise ValueError if scores is empty.
    """
    if not scores:
        raise ValueError("scores is empty.")
    return max(scores.values())
    """
    1. Optional を使うべきケース
    特徴 ）
    ・見つからないのが 想定内
    ・呼び出し側が None を普通に処理できる
    例 ）
    ・検索結果がない
    ・条件に合う人がいない
    ・データはあるけど「該当なし」
    👉 これは異常じゃない

    2.raise を使うべきケース
    特徴 ）
    ・その処理自体が 成立しない
    ・呼び出し側に「それはおかしい」と伝えたい
    例 ）
    ・平均を求めたいのにデータが空
    ・引数の型・値が意味をなさない



