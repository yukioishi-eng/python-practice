#Optional と空リストの組み合わせ
def top_scorers(scores: dict[str, int], min_score: int) -> Optional[list[str]]:
    """
    return a list of student names with the greatest score in list.
    rerurn None if no student meets the condition.
    """
    passed_students = {}
    for name, score in scores.items():
        if score >= min_score:
            passed_students[name] = score
    if not passed_students:
        return None
    
    #最高点はmax()で求める
    max_score = max(passed_students.values())
    top_students = []
    for name, score in passed_students.items():
        if score == max_score:
            top_students.append(name)
    return top_students
    #forとifが１つずつだったり、単純な構造の時は内包表記で書いた方が読みやすい可能性が高い

result = (top_scorers(scores, 69))
if result is None:
    print("No student meets the condition.")
else:
    print("Top students:",", ".join(result))    #括弧をなくしたいときは"(区切りたい文字列)".join(対象物)
