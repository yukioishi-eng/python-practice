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