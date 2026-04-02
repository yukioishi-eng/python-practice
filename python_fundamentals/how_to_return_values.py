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