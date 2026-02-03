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
#60点以上の点数の平均
def calc_avg(scores):
    total=0
    passed=[]
    for s in scores:
        if s>=60:
            passed.append(s)
            total+=s

    #passedは[]が入っているのでNoneにならない
    if len(passed)==0:
        return None         #存在しないということなので、0よりNoneが望ましい
    else:
        return total/len(passed)


#60点以上の点数の中で最大値
def max_pass_score(scores):
    passed=[]
    for s in scores:
        if s>=60:
            passed.append(s)

    #60点以上がないとき、Noneを返す
    if len(passed)==0:
        return None

    else:
        max_number=passed[0]
        for p in passed:
            if p>max_number:
                max_number=p
        return max_number
    #最初にmax_numberをNoneとすれば場合分けはいらない
    #変数名をmaxにすると同じ名前の関数があるので、不具合が起きやすくなるので、避けるべき
            
#戻り値を使う側の処理（Noneチェック）
scores1 = [55, 72, 90, 48, 66, 81]
max_number=max_pass_score(scores1)
if max_number is None:
    print("合格者はいません")
else:
    print(f"合格者の最高点は{max_number}点です")