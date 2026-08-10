#all(): すべての要素が真（True）か判定
print(all([True, True, True]))      # True
print(all([True, False, True]))     # False


#リスト内包表記: リストの要素管理を1行で書く
n = 2
distances = []
for _ in range(n - 1):
    d = int(input())
    distances.append(d)

distances = [int(input()) for _ in range(n - 1)]
#for文とif文が1つ以内で表現できる仕組みで活用することで、可読性が担保できる


#不等号の向き
#m >= aと書くよりa <= mと書いた方が直観的でわかりやすい


#for _ in range(n)
#変数に_を使用することで、rangeの引数の回数繰り返すという意味にできる


#文字列への代入
ans = ""
ans += "c"
#数式と同じように代入できる


#指定した位置の要素を削除し、値を取得
l = [0, 10, 20, 30, 40, 50]
popped_item = l.pop(0)
#こうすることで、lから0番目の要素を削除し、削除した値をpopped_itemに代入できる


#値からインデックスを取得
l = [0, 10, 20, 30, 40, 50]
index = l.index(30)
#引数に指定した値のインデックスを取得できる
#指定した値がリストに存在しない場合はValueErrorが発生するので注意
#in演算子で確認するか、try-except文で例外処理を行うと良い


#実際の数字とインデックスのズレ
#実際の数字は1から始まるが、インデックスは0から始まることが多い
#なので、受け取った数字を-1してからインデックスを指定するのがよい


#複数のリストの組み合わせ
name = ["A", "B", "C"]
age = [20, 30, 40]
for n, a in zip(name, age):
    print(n, a)

#リストの連続した組見合わせを探したいときには次のようなことにも使える
data = [1, 7, 3, 1, 4, 8, 1, 2, 3, 1, 4]
#リストの始まりを0, 1, 2としたリストを作成し、zipで組み合わせることで、連続した3つの要素を取得できる
#イテラブルの隣の要素と比較するときに使える
for a, b, c in zip(data, data[1:], data[2:]):
    if a == 3 and b == 1 and c == 4:
        print("314 found")


#リストの複数参照
data = [1, 7, 3, 1, 4, 8, 1, 2, 3, 1, 4]
for j in range(len(data) - 2):
    print(data[j:j+3])  #[1, 7, 3]
                        #[7, 3, 1]


#数値リストの文字列リストへの変換
data = [1, 7, 3, 1, 4, 8, 1, 2, 3, 1, 4]
print(list(map(str, data)))     #['1', '7', '3', '1', '4', '8', '1', '2', '3', '1', '4']


#リストの要素の文字列化と結合
print("".join(list(map(str, data))))    #17314812314


#joinのジェネレータ式を使った書き方
stamp = [
    ["abc", "def"],
    ["ghi", "jkl"]
]

sort_order = [1, 2, 1]
i = 0
print("".join(stamp[s - 1][i] for s in sort_order))
# 通常、for文は1つずつ値を取り出して処理するため、一見すると join() の引数として渡せないように見える。
# しかし、この書き方は「ジェネレータ式」と呼ばれ、 "abc" → "ghi" → "abc" を1つずつ生成する。
# join() は生成された文字列を順番に受け取り、 ["abc", "ghi", "abc"] が渡されたかのように連結して"abcghiabc" を返す。


#文字列の分割
s = "abc def ghi"
print(s.split())    #['abc', 'def', 'ghi']
#引数がなければ空白文字で分割される

time = "07:11"
print(time.split(":"))    #['07', '11']

text = "apple banana cherry"
print(text.split(None,1))    #['apple', 'banana cherry']
#split()の第2引数は最大分割数を指定できる


#イテラブルのインデックスと要素の取得
#最大値が複数ある時にenumerate()を用いる
num = [4, 2, 7, 14, 8, 14]
max_score = max(num)
#enumerateはインデックス、要素を取得する関数
result = [i for i, n in enumerate(num) if n == max_score]
print(result)    #[3, 5]


#アンパック演算子
#イテラブルを1つ開放する
#リストの要素を1つずつ展開して引数に渡すことができる
A = [1, 2, 3]
print(*A)    #1 2 3
print(*A, sep=",")    #1,2,3
print(*A, sep = "\n")    #1
                         #2
                         #3


#イテラブルの要素をカウント
l = [1, 2, 3, 1, 2, 1]
print(l.count(1))    #3

#Python標準ライブラリcollectionsにCounterクラスがある
#collections.Counter()にリストやタプルを渡すと、Counterオブジェクトが生成される
#Counterは辞書型dictのサブクラスで、キーに要素、値に出現回数という形のデータを持つ
#Counterに辞書型のkeys()やvalues()を使うこともできる

import collections
c = collections.Counter(l)
print(c)    #Counter({1: 3, 2: 2, 3: 1})
print(c[1])    #3
print(c.keys())    #dict_keys([1, 2, 3])

#most_common()メソッドを使うと、出現回数順に要素を取得できる
print(c.most_common(1))    #[(1, 3)]
print(c.most_common(2))    #[(1, 3), (2, 2)]
#most_common()の引数に整数を指定すると、上位n個の要素を取得できる
#most_common()を使用すると、要素がタプルの形になる


#組み合わせ
from itertools import combinations
data = [10, 20, 30, 40]
#dataの要素から3つ選ぶ組み合わせをcombにタプルとして代入する
for comb in combinations(data, 3):

    print(comb)     #(10, 20, 30)
                    #(10, 20, 40)
                    #(10, 30, 40)
                    #(20, 30, 40)

#すべての組み合わせなら次のようにできる
for i in range(1, len(data) + 1):
    for comb in combinations(data, i):

        print(comb)     #(10,)
                        #(20,)
                        #(30,)
                        #(40,)
                        #(10, 20)
                        #(10, 30)
                        #(10, 40)
                        #(20, 30)
                        #(20, 40)
                        #(30, 40)
                        #(10, 20, 30)
                        #(10, 20, 40)
                        #(10, 30, 40)
                        #(20, 30, 40)
                        #(10, 20, 30, 40)


#ジェネレータ式の応用
#行を店舗、列を書く商品として金額対照表
prices = [
    [1200, 800, 1500],
    [1100, 850, 1400],
    [1300, 900, 1600],
]

mean_A, mean_B, mean_C = (sum(p) // len(p) for p in zip(*prices))
#zipには1次元配列などのイテラブルが入るので、pricesをアンパックしている
#zipで作成したタプルの要素の返金を出し、変数に代入
#代入するときは左側の変数から行われる

print(mean_A, mean_B, mean_C)     #1200 850 1500


#for文とelse
data = ["Alice", "sam", "john"] 
for d in data:
    if d == "sum":
        print("discover")
        break

else:
    print("not applicable")
#これはfor文のbreakがされなかったときにはelseの処理をする
