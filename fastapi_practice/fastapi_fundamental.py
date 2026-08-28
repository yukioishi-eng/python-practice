from fastapi import FastAPI

app = FastAPI()

#@app.get()はFastAPIのルーティングデコレータで、HTTPのGETリクエストを受け取る
#引数にはドメイン以下のパスを入れる
@app.get("/")
def read_root():
    return {"message": "APIです"}