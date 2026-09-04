import requests

#getリクエストの送信
res = requests.get("http://127.0.0.1:8000/sample")
print(res.status_code)
print(res.text)    #{"message":"APIです"}
#検索エンジンのアドレスバーにhttp://127.0.0.1:8000/docsやhttp://127.0.0.1:8000/openapi.jsonなどを入力すると、APIの詳細がわかる
#自分が作ったAPIを外部と共有したいときなどに用いる

#パスパラメータを含むAPIへのリクエスト
res = requests.get("http://127.0.0.1:8000/items/110")
print(res.status_code)
print(res.text)    #{"items_id":"110","item_name":"Tシャツ"}
#パスにあった結果が出力されている

#処理の競合
res = requests.get("http://127.0.0.1:8000/items/sample")
print(res.status_code)
print(res.text)    #{"items_id":"sample","item_name":"Tシャツ"}
#read_itemとread_sample_itemで処理が競合するが、read_itemが上に書いてある方が優先される

#クエリパラメータを含むAPIへのリクエスト
res = requests.get("http://127.0.0.1:8000/items?step=2&limit=4")
print(res.status_code)
print(res.text)    #{"items":["スニーカー","靴下","パーカー"]}
#クエリパラメータは指定しないとエラーが起きる

#POSTリクエストの送信
res = requests.post("http://127.0.0.1:8000/items/", json = {"name": "Tシャツ", "price": 2000, "description": "白Tシャツ"})
print(res.status_code)
print(res.text)

#ヘッダを含むAPIへのリクエスト
res = requests.get("http://127.0.0.1:8000/sample/", headers = {"authorization": "Bearer 3v24vjd3"})
print(res.status_code)
print(res.text)     #{"message":"ヘッダー情報を受け取りました"}
print(res.headers)
#{'date': 'Wed, 02 Sep 2026 11:31:09 GMT', 'server': 'uvicorn', 'content-length': '56', 'content-type': 'application/json', 'custom-header': '12345'}
#'custom-header': '12345'が追加されている