#名前チェック関数（None または空文字）
def greet(name):
    if not name:
        print("名前を入力してください")
    else:
        print(f"こんにちは、{name}さん")    #f文を使うときはf文の外側に""はいらない

