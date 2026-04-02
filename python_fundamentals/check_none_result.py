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