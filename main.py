#学習ログ

"""
2026-01-31
内容：
・if文とfor文の復習
・リストから条件に合う要素を取り出す練習
"""
# 出現回数カウント → basics/count_numbers.py

"""
2026-02-01
内容：
リストから条件（60点以上）に合う要素を処理する練習
条件を満たす要素の個数をカウントする関数を実装
不要な条件分岐を書かないシンプルな実装を意識した
"""
# 出現回数カウント → basics/count_numbers.py

"""
2026-02-03
内容：
・条件付きで最大値を求める処理を実装
・None を使って「該当なし」の状態を表現する練習
・関数の戻り値を受け取り、if文で分岐する処理を復習
・エラーを避けるために戻り値のチェックを行う重要性を理解
"""
#条件下での平均 → calc_passed_avg.py
#条件下での最大値 → passed_score_max.py
#Noneチェック → check_none_result.py

"""
2026-03-04
内容：
・条件付きで最大値を求める処理を実装
・None を使って「該当なし」を表現
・関数の戻り値を if 文で分岐する処理を復習
・戻り値チェックの重要性を理解
"""
#Truthy / Falsyを用いたif文
data = []
if data:
    print("OK")
else:
    print("NG")

#Noneチェック関数
def check_none(x):
    if x is None:       #条件がxだけだとfalseyチェックになり、None以外の中身のない配列などもはじかれてしまう
        print("Noneです")
    else:
        print("値があります")

#Noneと空の区別
def judge(value):
    if value is None:
        print("None")
    elif not value:
        print("空")
    else:
        print("中身あり")

#点数判定
score = 78
if score >= 90:
    print("S")
elif score >= 60:   #90点以上はSなので、ここの条件で書かなくてよい
    print("合格")
else:
    print("不合格")

#名前チェック関数（None または空文字）
def greet(name):
    if not name:
        print("名前を入力してください")
    else:
        print(f"こんにちは、{name}さん")    #f文を使うときはf文の外側に""はいらない

