#60点以上の中で最高得点の人の名前を返す関数
scores = {
    "Alice": 58,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 45
}
def find_top_student(scores):  
    passed_members = {}
    for name, score in scores.items():    #辞書でキーと値を同時に使いたいときは.items()が必要  
        if score >= 60 :
            passed_members[name]=score
    if not passed_members:
        return None
    
    max_name = next(iter(passed_members))
    max_score = passed_members[max_name]
    #辞書で最初のキーが知りたいときはイテレータにしたあとにnext()
    #イテレータは順番に要素を取り出せるオブジェクト

    for name, score in passed_members.items():
        if score > max_score:
            max_score = score
            max_name = name
    return max_name

result = find_top_student(scores) 
if result is None:
    print("合格者なし")
else:
    print(f"最高得点者は{result}です")  
