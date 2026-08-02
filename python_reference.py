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
