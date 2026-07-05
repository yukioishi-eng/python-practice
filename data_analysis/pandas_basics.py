#pandasの基礎
#2次元の表形式データをDataFrame、DataFrameの1列分に相当する1次元のデータを Seriesという（Seriesにはカラムはない）
#列のラベルをColumn（カラム）という
#行を表す数字をインデックスという

import pandas as pd
pd.DataFrame({
    "名前": ["佐藤", "斎藤", "鈴木"],
})

#こうすることで、名前というカラム名の列が作成できた
#名前
#佐藤
#斎藤
#鈴木

pd.DataFrame({
    "名前": ["佐藤", "斎藤", "鈴木"],
    "年齢": ["21", "30", "18"]
}, index = ["i-1", "i-2", "i-3"])
#縦に並べることで、複数の列を作成できる
#インデックスを指定することができ、通常0から始まるインデックスを1から指定し、直観的にわかりやすくできる

#Excelファイルの読み込み

df = pd.read_excel(
    "C:/Users/31rek/python-practice/data_analysis/sample.xlsx", index_col = "ユーザID"    #"ファイルのパス", index_col = "インデックスに指定する列のカラム"
)
print(df)               #年齢   住所 血液型     
                #ユーザID                      
                #佐藤     21  東京都   O       
                #斎藤     30  埼玉県   A
                #鈴木     45  岐阜県  AB
                #田中     16  大阪府   O

#こうすることで、dfにExcelファイルのDataFrame化したものが入る
#列のカラム名を指定することで、その列をインデックスとみなせる ex.ユーザ名
#ほかにもcsv、json、xml、pickle、htmlデータも読み込める

#特定の行や列を抽出
df = pd.read_excel(
    "C:/Users/31rek/python-practice/data_analysis/sample.xlsx", index_col="ユーザID"
)
df_new = df.loc[["佐藤", "斎藤"], :]

print(df_new)       #   年齢   住所 血液型
                    #ユーザID             
                    #佐藤     21  東京都   O
                    #斎藤     30  埼玉県   A


#これで指定したインデックスとカラム名に合う列や行が抽出できる
#全ての行または列を指定するときは：、範囲指定をするときは最初：最後とすれば指定できる

df_oroginal = df.iloc[[0, 1, 2], [0]]

print(df_oroginal)      #ユーザID    
                        #佐藤     21
                        #斎藤     30
                        #鈴木     45

#ilocだと先頭を0とした行番号と列番号によって指定する

#条件抽出（ブールインデックス）
df = pd.read_excel("C:/Users/31rek/python-practice/data_analysis/sample.xlsx")
df_filtered = df[df["年齢"] >= 25]    #df[ブールインデックス]

print(df_filtered)  #  ユーザID  年齢   住所 血液型
                    #1    斎藤  30  埼玉県   A
                    #2    鈴木  45  岐阜県  AB

#ブールインデックスは真偽値（True/False）の配列を用いて、条件を満たすデータ要素のみを効率的に抽出・操作する手法
#複数条件を設定するときはdf[(条件1) & (条件2)]のように括弧でくくる

#統計量を調べる
df = pd.read_excel("C:/Users/31rek/python-practice/data_analysis/sample.xlsx")
print(df["年齢"].max())    #45

#他にも平均値や最小値など様々な値の取得ができる

#列単位で演算、追加
df = pd.read_csv("C:/Users/31rek/python-practice/data_analysis/sample.csv")
val = df["ポイント"] * df["レベル"]

print(val)      #0    13600
                #1    23000
                #2     3600

df["価値"] = df["ポイント"] * df["レベル"]
df["敬称"] = df["ユーザ名"] + "さん"

print(df)          #ID ユーザ名  ポイント  レベル     価値     敬称
             #0  ID001   ハル  3400    4  13600   ハルさん
             #1  ID009   リオ  4600    5  23000   リオさん
             #2  ID012  アキラ  1200    3   3600  アキラさん

#こうすることで、列の追加や文字列を結合しながら追加することもできる

#pandasの基礎の続き
#groupbyによる集計
import pandas as pd
df = pd.read_csv("C:/Users/31rek/python-practice/sales_data.csv")
print(df.groupby("担当者").mean(numeric_only=True))      #            売り上げ
                                                        #担当者               
                                                        #佐藤   199500.000000
                                                        #斎藤   233500.000000
                                                        #田中   223666.666667
#担当者別の売り上げ平均
#最近のpandasでは文字列を含む列がある時、meanにnumeric_only=Trueをいれて文字列を除外して計算するようにしないといけない
#欠損値は無視して計算できる

#インデックスの変更
df.index = [
    "2021/8/1",
    "2021/8/2",
    "2021/8/3",
    "2021/8/4",
    "2021/8/5",
    "2021/8/6",
    "2021/8/7",
    "2021/8/8",
    "2021/8/9"
]
df.index = range(1, 10)
#通常インデントは0から始まるが、1から始める設定をしている

#カラム名の変更
df.columns = ["date", "name", "sales"]

#指定したカラムのインデックス化
df_new = df.set_index("name")

print(df_new)    #          date   sales
                 #name                  
                 #佐藤    2021/8/1  203000
                 #斎藤    2021/8/2  215000
                 #田中    2021/8/3  190000
                 #佐藤    2021/8/4  186000
                 #田中    2021/8/5  239000
                 #佐藤    2021/8/6  210000
                 #斎藤    2021/8/7  252000
                 #田中    2021/8/8  242000
                 #佐藤    2021/8/9  199000

#set_indexは指定した列をインデックスとしたデータフレームを作成する
#なので、元のデータフレームは変更されない
#しかし、df.set_index("カラム名", inplace = True)とすると、df自体のインデックスを変更する

#インデックスを0から振りなおす
df_new = df_new.reset_index()

print(df_new)    #  name      date   sales
                 #0   佐藤  2021/8/1  203000
                 #1   斎藤  2021/8/2  215000
                 #2   田中  2021/8/3  190000
                 #3   佐藤  2021/8/4  186000
                 #4   田中  2021/8/5  239000
                 #5   佐藤  2021/8/6  210000
                 #6   斎藤  2021/8/7  252000
                 #7   田中  2021/8/8  242000
                 #8   佐藤  2021/8/9  199000

#これもdf.reset_index(inplace = True)とすると、dfが変更される
#しかし、元々インデックスだった列はインデックス変更後に新しい列として追加されるので、追加したくないときはdf.reset_index(inplace = True, drop = True)とすればよい

#データフレームの結合
df_1 = pd.DataFrame({
    "名前" : ["佐藤", "斎藤", "鈴木"],
    "年齢" : ["21", "30", "18"],
    "住所" : ["東京都", "岐阜県", "埼玉県"]
})

df_2 = pd.DataFrame({
    "名前" : ["秋山", "榎本"],
    "年齢" : ["19", "51"],
    "住所" : ["大阪府", "千葉県"]
})

df_new = pd.concat([df_1, df_2])

print(df_new)    #   名前  年齢   住所
                 #0  佐藤  21  東京都
                 #1  斎藤  30  岐阜県
                 #2  鈴木  18  埼玉県
                 #0  秋山  19  大阪府
                 #1  榎本  51  千葉県

#カラムが同じため、きれいに結合する

df_3 = pd.DataFrame({
    "名前" : ["秋山", "榎本"],
    "年齢" : ["19", "51"]
})
df_new = pd.concat([df_1, df_3])

print(df_new)    #   名前  年齢   住所
                 #0  佐藤  21  東京都
                 #1  斎藤  30  岐阜県
                 #2  鈴木  18  埼玉県
                 #0  秋山  19  NaN
                 #1  榎本  51  NaN

#カラムの数が異なる時、NaNとして結合される

df_1 = pd.DataFrame({
    "名前" : ["佐藤", "斎藤", "鈴木"],
    "年齢" : ["21", "30", "18"],
})

df_2 = pd.DataFrame({
    "レベル" : ["A", "B", "S"],
    "誕生日" : ["2/14", "9/30", "5/11"]
})
df_new = pd.concat([df_1, df_2], axis = 1)

print(df_new)    #   名前  年齢 レベル   誕生日
                 #0  佐藤  21   A  2/14
                 #1  斎藤  30   B  9/30
                 #2  鈴木  18   S  5/11

#横に結合したい場合はaxis = 1を付け加える
#しかし、行のデータが欠損したりすると、インデックスごとに上に詰めて結合されるので、ずれが発生したり、最後に行が足りなくなり、NaNが入ったりする

#内部結合
df_1 = pd.DataFrame({
    "id":   ["000A", "000E", "000Q", "000Y"],
    "年齢": [21, 30, 18, 22],
    "住所": ["東京都", "岐阜県", "埼玉県", "大阪府"]
})

df_2 = pd.DataFrame({
    "id":     ["000A", "000Q", "000E", "000Z"],
    "購入金額": [900, 1000, 5000, 7000]
})

df_new = pd.merge(df_1, df_2, on = "id")

print(df_new)    #     id  年齢   住所  購入金額
                 #0  000A  21  東京都   900
                 #1  000E  30  岐阜県  5000
                 #2  000Q  18  埼玉県  1000

#mergeは共通の列（id）の同じ要素の行を並列に結合する
#なので、2つのデータフレームに共通でないid（000Y, 000Z）の行は結合されていない。

#外部結合
df_new = pd.merge(df_1, df_2, on = "id", how = "left")

print(df_new)    #     id  年齢   住所    購入金額
                 #0  000A  21  東京都   900.0
                 #1  000E  30  岐阜県  5000.0
                 #2  000Q  18  埼玉県  1000.0
                 #3  000Y  22  大阪府     NaN

#howで指定したのdf_1のキーをすべて残し結合(左外部結合)

#右外部結合
df_new = pd.merge(df_1, df_2, on = "id", how = "right")

print(df_new)    #     id    年齢   住所  購入金額
                 #0  000A  21.0  東京都   900
                 #1  000Q  18.0  埼玉県  1000
                 #2  000E  30.0  岐阜県  5000
                 #3  000Z   NaN  NaN  7000

#条件付きの列追加
df_1 = pd.DataFrame({
    "id": ["000A", "000E", "000Q"],
    "年齢": [21, 30, 18]
})

df_1["区分"] = df_1["年齢"].map(lambda x: "成人" if x >= 20 else "未成年")

print(df_1)     #   id  年齢   区分
                #0  000A  21   成人
                #1  000E  30   成人
                #2  000Q  18  未成年

#map()は2種類の使い方があり、今回はpandasのSeriesが持っているメソッドSeries.map()
#map()は指定した列の要素を引数で与えた処理をしてから列を追加する関数(引数にはlambda、関数、辞書などが入る)
#lambdaは無名関数でその場で関数を作る
#指定した文字を引数とし、:後に関数の処理が入る
#"成人" if x >= 20 else "未成年"は三項演算子とも言い、値A if 条件 else 値Bで条件分岐が書ける

#組み込み関数のmap()
numbers = [1, 2, 3]
result = map(lambda x: x * 2, numbers)
print(list(result))    # [2, 4, 6]

#numbersの要素を一つ物取り出し、lambdaが2倍にして返す

#他のSeries.map()の使い方
df = pd.DataFrame({
    "手番号": [1, 2, 3, 4]
})
df["手"] = df["手番号"].map({1: "グー", 2: "チョキ", 3: "パー"})

print(df)    #   手番号    手
             #0    1   グー
             #1    2  チョキ
             #2    3   パー
             #3    4  NaN

#mapの引数に辞書を入れることでキーに対応した値で列を作成する
#どれとも合わない場合はNaNになる

df = pd.DataFrame({
    "手番号": [1, 2, 3, 4]
})
mapping = pd.Series(["グー", "チョキ", "パー"], index = [1, 2, 3])
df["手"] = df["手番号"].map(mapping)

print(df)    #   手番号    手
             #0    1   グー
             #1    2  チョキ
             #2    3   パー
             #3    4  NaN

#他のSeriesを渡すことで、インデックスで対応することもできる

#グラフ描画
import matplotlib.pyplot as plt
import japanize_matplotlib
df = pd.DataFrame({
    "名前": ["佐藤", "斎藤", "鈴木", "田中"],
    "年齢": [21, 30, 18, 26],
    "購入額": [9000, 8200, 1200, 5000]
})

df.plot(x = "名前", y = "購入額")
plt.show()

#matplotlibを用いると、DataFrameをグラフ化できる
#デフォルトは折れ線グラフ

df.plot(x = "名前", y = "購入額", kind = "bar")
plt.show()

#kindで指定すると、グラフ形式を変えることができる