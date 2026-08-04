#all(): すべての要素が真（True）か判定
print(all([True, True, True]))      # True
print(all([True, False, True]))     # False


#リスト内包表記: リストの要素管理を1行で書く
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
for a, b, c in zip(data, data[1:], data[2:]):
    if a == 3 and b == 1 and c == 4:
        print("314 found")
