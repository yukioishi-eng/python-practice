#最初に60以上の点数を返す関数
def find_pass(scores):
    for s in scores:
        if s>=60:
            return s
    #returnがされたら関数の処理が終了するので、breakはいらない
    return None     #60点以上がないときにNoneを返す

print(find_pass([45, 50]))
print(find_pass([45, 72, 88]))
scores = [45, 50, 59]

result = find_pass(scores)
if result is None:
    print("合格者なし")
else:
    print(f"合格者あり：{result}点")
