scores = {
    "Alice": 58,
    "Bob": 90,
    "Charlie": 90,
    "Diana": 45
}
def find_special_students(scores):
    max_score = scores[next(iter(scores))]
    for name, score in scores.items():
        if score > max_score:
            max_score = score
    if max_score < 60:
        return []
    
    #先に最高得点を求めて最高得点と同じ得点の人の名前をリストに入れる
    max_students = []
    for name, score in scores.items():
        if score == max_score:
            max_students.append(name)
    return max_students

print(find_special_students(scores))