#Web APIでデータ取得
#郵便番号検索API(https://zipcloud.ibsnet.co.jp/doc/api)を用いる
"""
リクエストURL: https://zipcloud.ibsnet.co.jp/api/search

リクエストパラメータ:
パラメータ名	項目名	           必須	    備考
zipcode	       郵便番号	           ○	   7桁の数字。ハイフン付きでも可。完全一致検索。
callback	   コールバック関数名	-	    JSONPとして出力する際のコールバック関数名。UTF-8でURLエンコードした文字列。
limit	       最大件数	           -	   同一の郵便番号で複数件のデータが存在する場合に返される件数の上限値（数字） ※デフォルト：20
"""
import requests
res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=1000001")
#データを取得するときは基本get(APIの詳細を確認)
#リクエストパラメータはリクエストUELの後ろに?を付けて入力し、キー = 値として入れる(複数ある場合は&で繋げる)
#resはレスポンスオブジェクト

print(res.status_code)
#これはリクエストのステータスコードを確認するコードで200バンダイなら成功
#400番台ならクライアント側のエラー(404 Not Found, 400 Bad Requestなど)、500番台ならサーバー側のエラー(500 Internal Server Errorなど)
print(res.text)
#文字列型でデータを出力

print(res.json())
#リクエストデータがjsonがたの際に用いる(辞書型)

res.get("https://zipcloud.ibsnet.co.jp/api/search", params = {"zipcode": "1000001"})
#リクエストパラメータが複数ある時、paramsに辞書として書くこともできる

#APIを利用するための認証
res.get("https:省略", headers = {"Authorization": "xxxxx"})
#基本この形が多い