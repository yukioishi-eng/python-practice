#別ファイルで呼び出す関数
def get_passed_names(scores: dict[str, int]) -> list[str]:
    return [name for name, score in scores.items() if score >= 60]

def find_top_student(scores: dict[str, int]) -> str | None:
    passed_members = {}
    for name, score in scores.items():   
        if score >= 60 :
            passed_members[name]=score
    if not passed_members:
        return None
    
    max_name = next(iter(passed_members))
    max_score = passed_members[max_name]

    for name, score in passed_members.items():
        if score > max_score:
            max_score = score
            max_name = name
    return max_name

def hello():
    print("Hello from students!")

if __name__ == "__main__":
    print("students loaded")



