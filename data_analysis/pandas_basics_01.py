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
    "C:/Users/31rek/python-practice/sample.xlsx", index_col = "ユーザID"    #"ファイルのパス", index_col = "インデックスに指定する列のカラム"
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
    "C:/Users/31rek/python-practice/sample.xlsx", index_col="ユーザID"
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
df = pd.read_excel("C:/Users/31rek/python-practice/sample.xlsx")
df_filtered = df[df["年齢"] >= 25]    #df[ブールインデックス]

print(df_filtered)  #  ユーザID  年齢   住所 血液型
                    #1    斎藤  30  埼玉県   A
                    #2    鈴木  45  岐阜県  AB

#ブールインデックスは真偽値（True/False）の配列を用いて、条件を満たすデータ要素のみを効率的に抽出・操作する手法
#複数条件を設定するときはdf[(条件1) & (条件2)]のように括弧でくくる

#統計量を調べる
df = pd.read_excel("C:/Users/31rek/python-practice/sample.xlsx")
print(df["年齢"].max())    #45

#他にも平均値や最小値など様々な値の取得ができる

#列単位で演算、追加
df = pd.read_csv("C:/Users/31rek/python-practice/sample.csv")
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
