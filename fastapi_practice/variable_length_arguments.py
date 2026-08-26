#可変長引数
def func1(*args):
    print(args)
func1(1, 3, 5)    #(1, 3, 5)
#可変長引数は関数の引数の数が決まっていないときに使う
#タプルとして関数に渡される

def func2(*args):
    result = "".join(args)
    print(result)
func2("a", "あ", "A")    #aあA

#通常の変数との併用
def func3(x, *args):
    print(x)
    print(args)
func3(1, "a", "f", 2)     #(a, f, 2) 
                          #1

#通常の変数を後に書く場合
def func4(*args, x):
    print(x)
    print(args)
func4("a", "f", 2, x = 1)     #(a, f, 2) 
                              #1
#通常の変数をキーワード引数として指定する必要がある

#辞書型で受け取る可変長引数
def func(**kwargs):
    print(kwargs)
func(name = "john", user_id = "02")                         #{'name': 'john', 'user_id': '02'}
func(name = "george", user_id = "25", balance  = 100)       #{'name': 'george', 'user_id': '25', 'balance': 100}

#変数名がキー、値がバリューとして辞書型を作成する
