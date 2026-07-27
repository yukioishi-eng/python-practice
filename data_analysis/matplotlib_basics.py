#matplotlibの基礎
#用語理解
#グラフを含む表示される画面をFigure、グラフをAxes、x軸とY軸をX axis、Y axis
#X軸とY軸のラベルをX axis label、Y axis label、目盛りをX axis ticks、Y axis ticks、凡例をlegend、罫線をgrid

import matplotlib.pyplot as plt
import japanize_matplotlib

# --- 1つ目のグラフ：基本の描画 ---

# Figureと複数のAxesを一度に作成する関数
# 主な引数：nrows/ncols(行・列数), figsize=(幅, 高さ), sharex/sharey(軸共有), tight_layout(自動調整)
fig, ax = plt.subplots()

# 第1引数にxの値、第2引数にyの値をリストで指定
ax.plot(["月", "火", "水", "木", "金", "土", "日"], [19, 22, 17, 25, 21, 27, 24])

# ラベルの指定
ax.set_xlabel("曜日")
ax.set_ylabel("気温")

plt.show()  # 表示


# --- 2つ目のグラフ：設定変更と応用 ---

# rcParamsはMatplotlibのデフォルト設定を変更する関数（ここではフォントサイズを変更）
# グラフを作成（plt.subplots）するより前に実行する必要がある
plt.rcParams["font.size"] = 14

fig, ax = plt.subplots()

ax.plot(["月", "火", "水", "木", "金", "土", "日"], [19, 22, 17, 25, 21, 27, 24], label = "最高気温")
ax.plot(["月", "火", "水", "木", "金", "土", "日"], [10, 13, 12, 10, 13, 11, 13], label = "最低気温")    #2つ目のグラフの追加
#ラベルは凡例の設定


ax.set_xlabel("曜日")

# rotation = "horizontal"でラベルを横並びに（垂直に指定したい場合は "vertical"）
ax.set_ylabel("気温", rotation="horizontal")

ax.set_title("東京10月1週目")  # タイトルの設定
ax.grid()    # グリッド線の追加
ax.legend()    #凡例の追加

plt.show()  # 表示


# --- 3つ目のグラフ：設定を追加 ---

plt.rcParams["font.size"] = 14

fig, ax = plt.subplots()

ax.plot(["月", "火", "水", "木", "金", "土", "日"], [19, 22, 17, 25, 21, 27, 24], label="最高気温")
ax.plot(["月", "火", "水", "木", "金", "土", "日"], [10, 13, 12, 10, 13, 11, 13], label="最低気温", marker = "o")
#marker = "o"でプロットの点を追加

ax.set_xlabel("曜日")
ax.set_ylabel("気温", rotation="horizontal")
ax.set_yticks([0, 5, 10, 15, 20, 25])    #Y軸の目盛りの変更
ax.set_title("東京10月1週目")
ax.grid()
ax.legend()

plt.show()

# --- 4つ目のグラフ：棒グラフ ---
plt.rcParams["font.size"] = 14

fig, ax = plt.subplots()

ax.bar(["月", "火", "水", "木", "金", "土", "日"], [19, 22, 17, 25, 21, 27, 24], label="最高気温")
ax.plot(["月", "火", "水", "木", "金", "土", "日"], [10, 13, 12, 10, 13, 11, 13], label="最低気温", marker = "o", color = "m")
#ax.bar()で棒グラフを作成
#color = "m"で棒グラフの色をマゼンタに変更

ax.set_xlabel("曜日")
ax.set_ylabel("気温", rotation="horizontal")
ax.set_yticks([0, 5, 10, 15, 20, 25])
ax.set_title("東京10月1週目")
ax.grid()
ax.legend()

plt.show()

# --- 5つ目のグラフ：散布図 ---
fig, ax = plt.subplots()
ax.scatter([120, 122, 122, 123, 125, 125, 126, 127, 128, 129, 129, 130],
           [21, 23, 22, 26, 21, 25, 28, 27, 28, 25, 31, 32])
#scatter()で散布図を作成

ax.set_xlabel('身長')
ax.set_ylabel('体重', rotation='horizontal')
ax.set_title('2年1組')
ax.grid()
plt.show()

#--- 6つ目のグラフ：ヒストグラム ---
fig, ax = plt.subplots()
ax.hist([21, 89, 34, 92, 12, 66, 34, 23, 66, 87, 65, 37, 56, 11], bins=5)
#hist()でヒストグラムを作成
#bins=5でヒストグラムの棒の数を指定(デフォルトは10)

ax.set_xlabel("点数")
ax.set_ylabel("人数", rotation="horizontal")
ax.set_title("2年1組")
ax.grid()
plt.show()

# --- 7つ目のグラフ：複数のグラフ、ファイル保存 ---
fig, ax = plt.subplots(2, 2, figsize=(15, 10))
#引数に(2, 2)を指定することで、2行2列のグラフを作成
#figsize=(15, 10)でグラフ全体のfigのサイズを指定

ax[0, 0].plot(["月", "火", "水", "木", "金", "土", "日"], [19, 24, 22, 26, 21, 25, 28])
#axは多次元配列なので、ax[行, 列]で各グラフにアクセスできる
ax[0, 0].set_title("ax[0, 0]のグラフ")
ax[0, 1].bar(["月", "火", "水", "木", "金", "土", "日"], [21, 11, 30, 21, 28, 22, 18])
ax[0, 1].set_title("ax[0, 1]のグラフ")
ax[1, 0].scatter([120, 122, 122, 123, 125, 125, 126, 127, 128, 129, 129, 130],
                  [21, 23, 22, 26, 21, 25, 28, 27, 28, 25, 31, 32])
ax[1, 0].set_title("ax[1, 0]のグラフ")
ax[1, 1].hist([21, 23, 22, 26, 21, 25, 28, 27, 28, 25, 31, 32], bins=5)
ax[1, 1].set_title("ax[1, 1]のグラフ")
plt.savefig("sample.png")
#plt.savefig()でグラフを画像として保存できる
#plt.show()でグラフを表示する前に保存する

plt.show()


