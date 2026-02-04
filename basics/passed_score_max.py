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
            