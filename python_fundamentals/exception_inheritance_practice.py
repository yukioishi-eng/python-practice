#例外の親クラス
class GameError(Exception):
    pass
class OutOfEnergyError(GameError):
    pass

try:
    raise OutOfEnergyError("エネルギー不足")
except OutOfEnergyError:
    print("エネルギー不足")