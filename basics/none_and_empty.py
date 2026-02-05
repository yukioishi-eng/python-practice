#Noneと空の区別
def judge(value):
    if value is None:
        print("None")
    elif not value:
        print("空")
    else:
        print("中身あり")