#numpyの基礎
import numpy as np

x_1 = np.array([1, 2, 3])
print(x_1 * 2)    #[2 4 6]

y = [1, 2, 3]
print(y * 2)    #[1, 2, 3, 1, 2, 3]
#ndarray（配列）のリストとの違いは配列の要素を簡単に加工できる、配列同士や行列計算ができる

#また、型についても異なる
print(type(x_1))    #<class 'numpy.ndarray'>
print(type(y))    #<class 'list'>

#そして、多次元の配列も作成可能
x_2 = np.array(
[[1, 2, 3],
 [4, 5, 6]]
)

#次元を調べる（ndim）
print(x_1.ndim)    #1
print(x_2.ndim)    #2

#各次元のサイズを調べる（shape）
print(x_1.shape)    #(3,)
print(x_2.shape)    #(2, 3)
#行列として数える

#要素がすべて0の配列（zeros）
print(np.zeros(3))    #[0. 0. 0.]
print(np.zeros((2, 3)))    #[[0. 0. 0.]
                            #[0. 0. 0.]]
#()の中身はshapeの時と同様に行列の数え方
#onesにすると、要素がすべて1

#要素がすべてランダムな値（0以上1未満）の配列
print(np.random.rand(3))   

#要素が空（メモリ上の値）の配列
print(np.empty(3))
#とりあえず配列だけ作っておきたい場合に用いる

#配列の計算
a = np.array(
[[1, 2, 3],
 [4, 5, 6]]
)
b = np.array(
[[1, 2, 3],
 [4, 5, 6]]
)
print(a + b)    #[[ 2  4  6]
                 #[ 8 10 12]]
#行か列のサイズがどちらかでもあっていれば計算可能
a = np.array([2, 3, 4])

b = np.array(
[[5, 6, 7],
[8, 9, 10]]
)
print(a + b)    #[[ 7  9 11]
                 #[10 12 14]]
#列のサイズが同じなので、行ごとに計算

a = np.array(
[[2],
 [3],
 [4]]
)

b = np.array(
[[10, 11],
 [12, 13],
 [14, 15]]
)
print(a + b)    #[[12 13]
                 #[15 16]
                 #[18 19]]
#行のサイズが同じなので、列ごとに計算

#行列の積（np.dot）
a = np.array(
[[1, 2, 3],
 [4, 5, 6]])

b = np.array(
[[2],
 [3],
 [4]]
)
print(np.dot(a, b))    #[[20]
                        #[47]]

#配列の変形（reshape）
x = np.array(
[[1, 2, 3],
 [4, 5, 6]]
 )
print(x.reshape(3, 2))    #[[1 2]
                           #[3 4]
                           #[5 6]]

#1次元の配列に変換（flatten）
print(x.flatten())    #[1 2 3 4 5 6]

#配列の要素にアクセス
print(x[0, :])    #[1 2 3]
print(x[:, 1])    #[2 5]
print(x[1,0])     #4

#配列の結合（concatenate）
y = np.array(
[[10, 11, 12],
 [13, 14, 15]]
)
print(np.concatenate([x, y], 0))    #[[ 1  2  3]
                                     #[ 4  5  6]
                                     #[10 11 12]
                                     #[13 14 15]]

print(np.concatenate([x, y], 1))    #[[ 1  2  3 10 11 12]
                                     #[ 4  5  6 13 14 15]]
#行（上下）で結合するときは0、列（左右）で結合するときは1を設定

#numpyの基本関数
#最初にnp.をつけてその後にmax, min, sumなどをつけることで指定した配列やリストの特性を知ることができる
print(np.prod(x))   #720（要素の積）
print(np.mean(x))   #3.5（要素の平均）
print(np.std(x))   #1.70782…（標準偏差）
print(np.var(x))   #2.91666…（分散）
print(np.median(x))   #3.5（中央値）

#数値単体に使える関数
print(np.log(1))    #0.0
print(np.sqrt(1))    #1.0
print(np.sin(0))    #0.0
print(np.cos(0))    #0.0
print(np.tan(0))    #0.0
print(np.pi)   #3.1415…