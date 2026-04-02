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