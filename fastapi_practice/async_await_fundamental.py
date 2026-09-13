#async / await 構文
#非同期処理とは処理の完了を待たずに次の処理を実行すること
import asyncio
import time
async def measurement():
    print(f"開始 {time.strftime('%X')}")
    await asyncio.sleep(1)
    await asyncio.sleep(2)
    print(f"終了 {time.strftime('%X')}")
    #開始 18:37:24
    #終了 18:37:27
#asyncをつけることでコルーチン(実行を中断して、あとから中断した場所から再開できるプログラム)となる
#awaitをつけることで、非同期処理の完了を待つことができる

if __name__ == "__main__":
    asyncio.run(measurement())
#__name__はPythonの組み込み変数で、スクリプトが直接実行された場合は "__main__" となる
#importされて実行された場合は、スクリプトのファイル名が入る
#if __name__ == "__main__"とは直接実行が起きた場合という条件である


#関数の切り出し
async def wait(wait_time):
#関数の処理内にawaitを使っているので、切り出した関数もコルーチンにする必要がある
    print(f"{wait_time}秒の待機を開始します")
    await asyncio.sleep(wait_time)
    return f"{wait_time}秒の待機が終了しました"

async def measurement1():
    print(f"開始 {time.strftime('%X')}")
    result_1 = await wait(1)
    #コルーチンの関数にもawaitをつける
    result_2 = await wait(2)
    print(result_1)
    print(result_2)
    print(f"終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(measurement1())


#並行処理
async def measurement2():
    print(f"開始 {time.strftime('%X')}")
    task1 = asyncio.create_task(wait(1))
    task2 = asyncio.create_task(wait(2))
    #create_task()を使うことで、非同期処理を並行して実行できる
    await task1
    await task2
    #taskは並列処理される(2秒の待機となる)
    print(f"{task1.result()}")
    print(f"{task2.result()}")
    print(f"終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(measurement2())


#複数のコルーチンやタスクの並列処理(gather)
async def measurement3():
    print(f"開始 {time.strftime('%X')}")
    task1 = asyncio.create_task(wait(1))
    results = await asyncio.gather(wait(2), task1)
    #複数のコルーチン(wait(2))やタスク(task1)をまとめて並列処理し、結果をまとめて取得できる

    print(results)    #['2秒の待機が終了しました', '1秒の待機が終了しました']
    #受け取った結果をリストにする

    print(f"終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(measurement3())


#通常の関数を非同期関数に変換する
async def wait2(sec):
    print(f"{sec}秒の待機を開始します")
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, time.sleep, sec)
    #run_in_executor()を使うことで、通常の関数(time.sleep)を非同期関数として実行できる

    return f"{sec}秒の待機が終了しました"

if __name__ == "__main__":
    asyncio.run(wait2(3))


#タイムアウト
async def measurement4():
    print(f"開始 {time.strftime('%X')}")
    try:
        results = await asyncio.wait_for(wait2(5), timeout=3)
        #wait_for()を使うことで、指定した時間内に処理が完了しなかった場合にTimeoutErrorを発生させることができる

        print(results)
    except asyncio.TimeoutError:
        print("タイムアウト")
    print(f"終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(measurement4())