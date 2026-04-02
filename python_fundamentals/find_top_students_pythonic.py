#max()を用いたPythonicな処理
scores = {
    "Alice": 80,
    "Bob": 90,
    "Charlie": 90,
    "David": 50
}
def find_top_students(scores, min_score):   #引数に合格点min_scoreをとる
    passed_students = {}
    for name, score in scores.items():
        if score >= min_score:
            passed_students[name] = score
    if not passed_students:
        return []
    max_score = max(passed_students.values())  #辞書のキーとバリューを知りたいときは.keys(),.value()
    
    return [name for name, score in passed_students.items() if score == max_score]
    
print(find_top_students(scores, 46))