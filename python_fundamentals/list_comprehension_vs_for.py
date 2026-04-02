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