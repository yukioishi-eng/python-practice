#Noneチェック関数
def check_none(x):
    if x is None:       #条件がxだけだとfalseyチェックになり、None以外の中身のない配列などもはじかれてしまう
        print("Noneです")
    else:
        print("値があります")
