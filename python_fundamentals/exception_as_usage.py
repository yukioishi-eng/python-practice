#as eの使い方
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"残高{balance}円で{amount}円は引き出せません")


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


try:
    withdraw(1000, 5000)
except InsufficientFundsError as e:
    print("エラー発生")
    print("現在残高:", e.balance)   #1000
    print("要求額:", e.amount)    #5000
    print("メッセージ:", e)    #残高1000円で5000円は引き出せません


#eにはインスタンスが保存される
#sそして、print(e)とすると、内部でstr(e)を呼ぶので、タプルが文字列として変換され、文字列単体が出力される
#print(e.args[0])とすることでも文字列が出せる

