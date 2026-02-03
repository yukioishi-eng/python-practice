#60点以上の点数をカウント
def count_pass(scores):
    cnt=0
    for s in scores:
        if s>=60:
            cnt+=1
    #最初にcntがNoneの時の対応を考えていたが、3行に0を代入しているので、Noneにはならない
    return cnt