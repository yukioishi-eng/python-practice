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