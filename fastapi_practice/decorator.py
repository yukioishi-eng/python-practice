#デコレータの基本
#デコレータとは関数に対して、コードの中身を変えずに処理を追加したり変更するもの

def start_end(func):
    def add_start_end(text):
        print("start")
        func(text)
        print("end")
    return add_start_end


@start_end
def add_hello(text):
    print("hello " + text)

add_hello("mother")

#処理の流れ：
#@start_endによって、add_hello関数がstart_end関数に渡される
#add_helloという名前が返されたadd_start_end関数を参照するようになる
#add_hello("mother")を実行すると、実際にはadd_start_end("mother")が実行される
#なので、呼び出し側が関数を呼び出しているんだけど、中身はデコレータの処理の中で関数が呼び出され、デコレータの処理を出力している

#変数の数が決まっていない場合のデコレータ
def start_end(func):
    #可変長引数の2つの場合で書くことで、キーワード引数でも対応できる
    def add_start_end(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return add_start_end

@start_end
def no_solution():
    print("解なし")

@start_end
def print_join_dash(a, b):
    print(f'{a}-{b}')

no_solution()
print_join_dash('163', b='8001')

#デコレータ側の引数を可変長引数にすることで、デコレートする関数の引数の数に縛られず、処理を行える

#戻り値がある関数の場合
def start_end(func):
    def add_start_end(*args, **kwargs):
        #関数の戻り値を受け取ってあげることで、xを使える状態にしつつ、デコレータの処理を行える
        print('start')
        x = func(*args, **kwargs)
        print('end')
        return x
    return add_start_end

@start_end
def plus_1(a):
    print("plus_1が実行されました")
    return a + 1

x = plus_1(4)
print(x)    #start
            #plus_1が実行されました
            #end
            #5

