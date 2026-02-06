#学習ログ

"""
2026-01-31
内容：
・if文とfor文の復習
・リストから条件に合う要素を取り出す練習
"""
# 条件に合うデータの抽出 → basics/passed_number.py

"""
2026-02-01
内容：
リストから条件（60点以上）に合う要素を処理する練習
条件を満たす要素の個数をカウントする関数を実装
不要な条件分岐を書かないシンプルな実装を意識した
"""
# 条件下での出現回数カウント → basics/count_numbers.py

"""
2026-02-03
内容：
・条件付きで最大値を求める処理を実装
・None を使って「該当なし」の状態を表現する練習
・関数の戻り値を受け取り、if文で分岐する処理を復習
・エラーを避けるために戻り値のチェックを行う重要性を理解
"""
#条件下での平均 → basics/calc_passed_avg.py
#条件下での最大値 → basics/passed_score_max.py
#Noneチェック → basics/check_none_result.py

"""
2026-02-04
内容：
・Truthy / Falsy を用いた if 文の挙動を確認
・None を明示的に判定する条件分岐を実装
・None と 空（空リスト・空文字など）を区別する処理を理解
・条件の順序を意識した if / elif / else の書き方を練習
・入力値（名前）が None または空の場合の入力チェック処理を実装
"""
#Truthy / Falsyを用いたif文 → basics/truthy_falsy_if.py
#Noneチェック関数 → basics/none_check.py
#Noneと空の区別 → basics/none_and_empty.py
#点数判定 → basics/score_judgement.py
#名前チェック関数（None または 空文字）→ basics/name_check.py

"""
2026-02-05
内容：
・for文とif文を組み合わせて、条件に合う要素を抽出する処理を実装
・条件に合う値が見つからない場合、None を返す関数を作成
・関数の戻り値を受け取り、None チェックで安全に分岐する処理を復習
"""
#最初に60以上の点数を返す関数 → first_pass_score.py

"""
2026-02-06
内容：
・辞書（名前 → 点数）を使った条件付きデータ抽出の復習
・単一結果では None、複数結果では空リスト [] を返す設計の使い分けを理解
・next(iter(dict)) を用いた初期値設定の考え方を確認
・最高得点者が複数いる場合に全員を返す処理を実装
・max() を用いた Pythonicな最大値取得方法を学習
・max(dict) / max(dict.values()) / max(dict, key=...) の違いを理解
"""
#辞書から60点以上の人の名前を表示
scores = {
    "Alice": 58,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 45
}
passed_member = []
for name, score in scores.items():    #辞書でキーと値を同時に使いたいときは.items()が必要
    if score >= 60 :
        passed_member.append(name)
print(passed_member)

#60点以上の中で最高得点の人の名前を返す関数
scores = {
    "Alice": 58,
    "Bob": 72,
    "Charlie": 90,
    "Diana": 45
}
def find_top_student(scores):
    passed_members = {}
    for name, score in scores.items():
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

#最高得点の人が複数いる場合の処理
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