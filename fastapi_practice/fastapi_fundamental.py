#FastAPIの基礎
#client.pyからリクエストを送る
from fastapi import FastAPI

app = FastAPI()

@app.get("/sample")
#@app.get()はFastAPIのルーティングデコレータで、HTTPのGETリクエストを受け取る
#引数にはドメイン以下のパスを入れる
#パスは処理を識別するもの   
def read_root():
    return {"message": "APIです"}

#パスが可変なAPI
@app.get("/items/{items_id}")
def read_item(items_id):
#パスのitems_idに入れたものが関数の引数に代入される

    return {"items_id": items_id, "item_name": "Tシャツ"}
    #一般的にキーと値の組で出力するので、辞書型が望ましい

@app.get("/items/sample")
def read_sample_item():
    return {"item_id": "サンプルデータ"}
#read_itemとread_sample_itemで処理が競合するが、read_itemが上に書いてある方が優先される

#クエリパラメータ
from fastapi import Query
from typing import Annotated

items = ["Tシャツ", "スカート", "スニーカー", "靴下", "パーカー"]
#通常はデータベース管理

@app.get("/items")
def read_items(step: int, limit: Annotated[int, Query(ge = 1, le = 10)] = 10):
    #Annotatedは型ヒントに追加のメタデータをくっつける仕組み
    #Queryは指定した引数がクエリパラメータ(パスの?以降のキー＝値のこと)であることとバリデーションルールをFastAPIに伝える役割
    #geで以上、leで以下、gtでより大きい、ltでより小さい
    
    return {"items": items[step: step + limit]}
    #[step: step + limit]はイテラブルのインデックス範囲を超えても実際の長さに抑えられる

#データの送信(POST)
from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str = Field(None, max_length = 100)
    #Fieldは変数の設定をすることができ、FastAPIの設定に加え、min_length　最小文字数(str)、max_length　最大文字数(str)、max_digits	最大桁数などがある
    #第1引数でデフォルト設定ができる

    price: float = Field(lt = 99999999)
    description: Optional[str]  = None
    #Optionalはデータ型がNoneでも良いときに用いる(Union[str, None]と同義)
#BaseModelは自動的にインスタンス作成時にデータ型のバリデーションをしたりする

@app.post("/items/")
def create_item(item: Item):
    print(f"データを登録します：{item.name}, {item.price}, {item.description}")
    return item

#ヘッダー
#ヘッダとは通信時に送信することで通信の制御や認証などに使われる情報(郵便でいう宛名や差出人、郵便番号などの情報)
#ヘッダーは通信の中継ソフトウェアとサーバ側で受け取られ、処理が行われる

#                           HTTPヘッダー早見表
# ヘッダー名           | 役割                          | 例
# --------------------|-------------------------------|----------------------------------------
# Host                | どのドメイン宛かを示す          | Host: example.com
# User-Agent          | クライアントの種類を示す         | User-Agent: Mozilla/5.0
# Accept              | 受け取りたいデータ形式を伝える     | Accept: application/json
# Content-Type        | ボディのデータ形式を伝える        | Content-Type: application/json
# Content-Length       | ボディのバイト数                | Content-Length: 348
# Authorization       | 認証情報(誰からのリクエストか)    | Authorization: Bearer eyJhbGc...
# Cookie              | クライアントが保持するCookieを送信 | Cookie: session_id=abc123
# Set-Cookie          | サーバーがCookieを設定           | Set-Cookie: session_id=abc123; HttpOnly
# Cache-Control       | キャッシュの可否・期限を指定       | Cache-Control: no-cache
# ETag                | リソースのバージョン識別子        | ETag: "33a64df5"
# Accept-Encoding     | 対応する圧縮方式を伝える          | Accept-Encoding: gzip, deflate
# Content-Encoding     | ボディの圧縮方式を伝える          | Content-Encoding: gzip
# Referer             | どのページから遷移してきたか       | Referer: https://example.com/page
# Origin              | リクエスト元のオリジン(CORS用)    | Origin: https://example.com
# X-Request-ID        | リクエストの追跡用ID(独自拡張)    | X-Request-ID: 7f3e2b1a
# X-API-Key           | APIキーによる認証(独自拡張)      | X-API-Key: abcdef123456
# ============================================================
from fastapi import Header, Response

@app.get("/sample/")
def read_sample(
        response: Response,
        authorization: Annotated[Optional[str], Header()] = None
    #デフォルト値がない変数はある変数の前に定義する必要がある(pythonの仕様)
):
    #authorizationは認証・認可をするための情報
    #authorizationヘッダーの値を受け取る。もし送られてこなければNone
    #ヘッダ名は大文字にしても小文字にしても受け取れる
    #ヘッダ名は標準化されているので、大文字小文字の違い以外は変えることができない

    print(authorization)
    response.headers["custom-header"] = "12345"
    #レスポンスヘッダーへの追加
    #レスポンスヘッダーとはサーバーがクライアントに送信するヘッダー情報のことを指す
    return {"message": "ヘッダー情報を受け取りました"}
