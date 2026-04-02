#Optional と空リストの使い分け
def students_above_threshold(scores: dict[str, int], threshold: int) -> list[str]:
    """
    Return a list of student names with scores >= threshold.
    Returns an empty list if no student meets the condition.
    """
    passed_students = []
    for name, score in scores.items():
        if score >=threshold:
            passed_students.append(name)
    return passed_students

scores = {"Alice": 80, "Bob": 90, "Charlie": 90, "David": 50}

print(students_above_threshold(scores, 60))  # ['Alice', 'Charlie']
print(students_above_threshold(scores, 100)) # []
