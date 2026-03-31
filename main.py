#学習ログ

"""
2026-01-31
内容：
・if文とfor文の復習
・リストから条件に合う要素を取り出す練習
"""
# 条件に合うデータの抽出 → basics/passed_number.py

"""
2026-02-01
内容：
・リストから条件（60点以上）に合う要素を処理する練習
・条件を満たす要素の個数をカウントする関数を実装
・不要な条件分岐を書かないシンプルな実装を意識した
"""
# 条件下での出現回数カウント → basics/count_numbers.py

"""
2026-02-03
内容：
・条件付きで最大値を求める処理を実装
・None を使って「該当なし」の状態を表現する練習
・関数の戻り値を受け取り、if文で分岐する処理を復習
・エラーを避けるために戻り値のチェックを行う重要性を理解
"""
#条件下での平均 → basics/calc_passed_avg.py
#条件下での最大値 → basics/passed_score_max.py
#Noneチェック → basics/check_none_result.py

"""
2026-02-04
内容：
・Truthy / Falsy を用いた if 文の挙動を確認
・None を明示的に判定する条件分岐を実装
・None と 空（空リスト・空文字など）を区別する処理を理解
・条件の順序を意識した if / elif / else の書き方を練習
・入力値（名前）が None または空の場合の入力チェック処理を実装
"""
#Truthy / Falsyを用いたif文 → basics/truthy_falsy_if.py
#Noneチェック関数 → basics/none_check.py
#Noneと空の区別 → basics/none_and_empty.py
#点数判定 → basics/score_judgement.py
#名前チェック関数（None または 空文字）→ basics/name_check.py

"""
2026-02-05
内容：
・for文とif文を組み合わせて、条件に合う要素を抽出する処理を実装
・条件に合う値が見つからない場合、None を返す関数を作成
・関数の戻り値を受け取り、None チェックで安全に分岐する処理を復習
"""
#最初に60以上の点数を返す関数 → first_pass_score.py

"""
2026-02-06
内容：
・辞書（名前 → 点数）を使った条件付きデータ抽出の復習
・単一結果では None、複数結果では空リスト [] を返す設計の使い分けを理解
・next(iter(dict)) を用いた初期値設定の考え方を確認
・最高得点者が複数いる場合に全員を返す処理を実装
・max() を用いた Pythonicな最大値取得方法を学習
・max(dict) / max(dict.values()) / max(dict, key=...) の違いを理解
"""
#60点以上の中で最高得点の人の名前を返す関数 → find_top_student.py
#最高得点の人が複数いる場合の処理 → find_top_students.py
#max()を用いたPythonicな処理 → find_top_students_pythonic.py

"""
2026-02-07
内容：
・型ヒント（dict[str, int], list[str], str | None）の書き方を練習
・docstring を用いて関数の役割・引数・戻り値を明示
・フォルダ分割を行い、別ファイルの関数を import して使用
・if __name__ == "__main__": を使い、実行用コードとロジックを分離
"""
#型ヒント＋docstring（読み手を意識したコード) → practice_typehint_docstring.py
#型ヒントの設定練習 → practice_typehint.py
#ファイル分割 ＋ import → run_import_students.py
#if __name__ == "__main__"の使い方 → if_main_demo.py

"""
2026-02-08
内容：
・Optional の意味と使い方を理解
・返り値設計の使い分けを学習
・型ヒント付き関数の実装練習
・Pythonic な書き方の理解
・Optional の返り値を呼び出し側で安全に扱う方法
"""
#Optional を用いた関数 → first_over_threshold_optional.py
#Optional と空リストの使い分け → students_above_threshold_list.py
#Optional と空リストの組み合わせ → top_scorers_optional_list.py

"""
2026-02-09
内容：
・Optional の意味と使いどころの理解
・raise ValueError の書き方と設計意図
・Optional と raise の使い分け判断
・型ヒントと返り値設計の整合性チェック
"""
#通常の書き方と内包表記の書き方の比較 → list_comprehension_vs_for.py
#Optional / 空リスト / 例外 のどれを返すべきか → how_to_return_values.py
#Optionalとraiseの設計判断 → optional_vs_raise_design.py

"""
2026-02-10
内容：
・dict の基本構造（key: value）と dict in dict の扱い方
・値と型の検証方法（isinstance）
・isinstance(value, int) を用いたデータ不整合チェック
・Optional と例外の設計判断（「起こりうる結果なし」→ None、「データ不整合・成立しない状態」→ raise ValueError）
・年齢制限つきユーザー取得関数を設計・実装
・存在チェック → データ検証 → ビジネス条件 の順で if を構成
・コメントの書き方の指針（判断理由・意味 → 改行コメント、補足説明 → 横コメント）
"""
#ユーザー検索APIのコアロジック → user_search_core.py
#年齢制限つきユーザー取得 → adult_user_optional.py

"""
2026-02-11
内容：
・dict in dict の理解とアクセス方法の確認
・dict.get() の挙動理解（KeyErrorとの違い）
・Optional を返す関数の設計
・None 伝播パターンの実装（3段チェーン）
・Optional を返す関数の安全な組み合わせ
・None と raise ValueError の使い分け
・重複関数呼び出しを避ける設計
・責務分離を意識した関数構成
"""
#Optionalを返す関数を組み合わせる → optional_function_composition.py 
#3段の組み合わせ → optional_three_step_chain.py

"""
2026-02-12
内容：
・classの概要の理解
・コンストラクタでのバリデーション実装
・メソッドの self の役割を理解
・updateメソッドの設計を学習
・privateメソッド（_validate_xxx）の設計意図を理解
・クラス設計での責務整理を意識できるようになった
"""
#classの概要 → class_basics_dog.py
#classの演習 → user_class_design.py

"""
2026-02-13
内容：
・@property を使うことで、メソッドを属性のように読み取れることを理解した
・getter は属性の「読み取り時」に自動で呼び出される処理であることを理解した
・self.age = value は通常の代入ではなく、setter を経由することを理解した
・実際の保存は _age のような private 属性に行う必要がある理由（無限ループ防止）を理解した
・_name, _age, _email のように内部保存用属性と公開用 property を分離する設計を学んだ
・初期化 (__init__) と更新の両方で setter を使うことで、一貫した validation を保証できることを理解した
・name, age, email を property + setter + validation で管理する User クラスを実装した
・カプセル化（内部状態を直接触らせず、安全な窓口だけ公開する設計）の基本を理解した
"""
#propertyを使ったclass処理 → property_class_design.py

"""
2026-02-14
内容：
・private属性（_owner, _balance, _transactions）によるカプセル化を理解
・property を使い「参照は可能・直接代入は不可」を実現
・残高の変更を apply_transaction() のみに限定し、状態変更の責務を集中させた
・Transactionを検証付きの値オブジェクトとして扱う考え方を理解
・取引履歴を list で保持し、外部公開時は tuple に変換して不変化
・mutable（list）と immutable（tuple）の違いと用途を理解
・不変条件（invariant）をクラスが保証する設計の重要性を理解
"""
#propertyを用いた計算プロパティ（area, full_name）を追加するクラス設計の発展練習 → computed_property_practice.py
#「安全な状態管理」と「不変条件の維持」 → state_management_and_invariants.py

"""
2026-02-15
内容：
・例外設計をすることで可読性とエラーごとの処理を可能にする
・継承設計によるエラーの分岐を理解
・as eの利点と多様な使い方を理解
"""
#例外設計 → bank_account_exception_design.py
#例外の親クラス → exception_inheritance_practice.py
#as eの使い方 → exception_as_usage.py

"""
2026-02-17
内容：
・Service / Domain の責務分離を意識した設計演習を行った
・購入処理を User・Product・PurchaseService に分割した
・「誰の責任か？」を基準にロジックの置き場所を考えた
・支払いロジックは User の責任であることを理解した
・不整合を防ぐために「変更前チェック」を意識した
・動くコードよりも「設計の正しさ」が重要だと学んだ
"""
#実務を意識した設計演習 → purchase_service_design.py

"""
2026-02-18
内容：
・オブジェクト指向での責務分離を意識して設計を行った
・副作用（状態変更）の順番によって不整合が起こることを学んだ
・例外クラスをドメインごとに定義する重要性を確認
・クーポン割引ロジックを独立したクラスに分離
・コードをシンプルに書くことで、エラー箇所を特定しやすくなると理解
"""
#テストしやすい設計 → domain_service_design_practice.py
"""
2026-02-19
内容：
・Order と CheckoutService の責務分離
状・態管理の導入
Cou・ponを任意にする設計
pytest導入・実行確認
・例外テスト作成
・with pytest.raises() の意味を理解
・成功時／失敗時の副作用確認の重要性を理解
"""
#トランザクションの中心に Order を置く設計

"""
2026-02-23
内容：
・Order中心のトランザクション設計を状態機械に進化させた
・Enum（OrderStatus / OrderAction）で状態と操作を型安全に管理
・状態遷移を if 文から辞書（ALLOWED_TRANSITIONS）へ移行
・_transition() を導入し状態変更を一本化
・副作用（支払い・在庫減少）と状態遷移の順序を整理
・ドメイン例外の階層設計を検討（OrderError基底クラス）
"""
#状態遷移の高度化

"""
2026-02-24
内容：
・pay() の原子性を改善
・チェック → 副作用 → 状態確定 の順序
・二重支払い・二重キャンセル防止
・テストを通して設計の整合性を確認
"""
#原子性と状態遷移の制御による、不整合を許さない堅牢な注文管理システムの設計

"""
2026-02-25
内容：
・状態遷移テーブル（ALLOWED_TRANSITIONS）にロジックを集約
・状態チェックを if 文からテーブル駆動へ移行
・副作用を クリティカル / ノンクリティカル に分類
・原子性の範囲を「ビジネス整合性」に限定する設計を理解
・例外を握り潰さず、トランザクション境界で扱う考え方を整理
・ドメイン層は「正しい振る舞い」を定義し、原子性保証はApplication/DB層の責務と理解
・cancel処理を「返金・在庫復元・状態変更」の1事実として設計
・レイヤードアーキテクチャ的責務分離を意識
"""
#状態遷移モデルと副作用の分離による堅牢な注文ドメイン設計

"""
2026-03-08
内容：
・ドメインイベントの設定
・DDD設計に合わせたプログラム設計
"""

"""
2026-03-09
内容：
・PayOrderUseCase でイベントを処理し、副作用（レシート送信）をドメインから分離
・Order を Aggregate Root として設計し、User・Product などの整合性を管理
・Order.pay() を通してのみ状態変更を行い、Aggregateの整合性を保証
・ReceiptSender を インターフェース化して依存を抽象化
・送信方法（Email / Slack など）を ポリモーフィズムで差し替え可能に設計
・Domain → Application → Infrastructure の 依存方向を意識
・id(self) は一時的識別子であり、本来はドメインIDを持つべきと理解
"""

"""
2026-03-13
内容：
Repositoryパターン導入
OrderRepository を抽象クラスとして定義
InMemoryOrderRepository を実装
execute() でorder_repo.get()、order_repo.save()の実装
EmailReceiptSender、SlackReceiptSender、LINEReceiptSender
transition を最後にする理由
Aggregateの整合性を守る
1 Transaction = 1 Aggregate（設計上の重要ルール）
"""

"""
2026-03-24
内容：
イベント処理の完成
Repositoryの不備修正
永続化漏れ修正（バグ修正）
ドメインイベント強化
EntityにID追加
Orderの責務整理
バグ修正（動作面）
"""
#ドメイン層
from abc import ABC, abstractmethod
from typing import Optional


#例外
class OrderError(Exception):
    pass

class OutOfStockError(OrderError):
    pass

class InsufficientBalanceError(OrderError):
    pass

class InvalidStateTransitionError(OrderError):
    pass


#ドメインイベント
class DomainEvent:
    pass

class OrderPaid(DomainEvent):
    def __init__(self, order_id, amount: int):
        self.order_id = order_id
        self.amount = amount


#ValueObject
class OrderId:
    def __init__(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise ValueError("OrderId is invalid")
        self._value = value

    @property
    def value(self):
        return self._value

    def __eq__(self, other):
        return isinstance(other, OrderId) and self.value == other.value


#Repository interface
class OrderRepository(ABC):
    @abstractmethod
    def get(self, order_id: OrderId):
        pass

    @abstractmethod
    def save(self, order):
        pass


class UserRepository(ABC):
    @abstractmethod
    def get(self, user_id):
        pass

    @abstractmethod
    def save(self, user):
        pass


class ProductRepository(ABC):
    @abstractmethod
    def get(self, product_id):
        pass

    @abstractmethod
    def save(self, product):
        pass


#Entity
class Product:
    def __init__(self, product_id, price: int, stock: int):
        if price < 1:
            raise ValueError()
        if stock < 0:
            raise ValueError()

        self.id = product_id
        self._price = price
        self._stock = stock

    @property
    def price(self):
        return self._price

    def decrease_stock(self):
        if self._stock == 0:
            raise OutOfStockError()
        self._stock -= 1

    def return_product(self):
        self._stock += 1


class User:
    def __init__(self, user_id, balance: int):
        if balance < 0:
            raise ValueError()

        self.id = user_id
        self._balance = balance

    def pay(self, amount: int):
        if self._balance < amount:
            raise InsufficientBalanceError()
        self._balance -= amount

    def refund(self, amount: int):
        self._balance += amount


class Coupon:
    def __init__(self, discount_amount: int):
        if discount_amount < 1:
            raise ValueError()
        self._discount_amount = discount_amount

    def apply(self, price):
        if self._discount_amount > price:
            raise ValueError()
        return price - self._discount_amount


# --- Order ---
from enum import Enum, auto

class OrderStatus(Enum):
    CREATED = auto()
    PAID = auto()
    SHIPPED = auto()
    CANCELED = auto()

class OrderAction(Enum):
    PAY = auto()
    CANCEL = auto()
    SHIP = auto()

ALLOWED_TRANSITIONS = {
    OrderStatus.CREATED: {
        OrderAction.PAY: OrderStatus.PAID,
        OrderAction.CANCEL: OrderStatus.CANCELED,
    },
    OrderStatus.PAID: {
        OrderAction.SHIP: OrderStatus.SHIPPED,
        OrderAction.CANCEL: OrderStatus.CANCELED,
    },
    OrderStatus.SHIPPED: {},
    OrderStatus.CANCELED: {},
}


class Order:
    def __init__(self, order_id, user_id, product_id, coupon: Optional[Coupon] = None):
        self._id = order_id
        self._user_id = user_id
        self._product_id = product_id
        self._coupon = coupon
        self._status = OrderStatus.CREATED
        self._events = []
        self._paid_amount = 0

    @property
    def id(self):
        return self._id

    @property
    def user_id(self):
        return self._user_id

    @property
    def product_id(self):
        return self._product_id

    @property
    def events(self):
        return list(self._events)

    def clear_events(self):
        self._events.clear()

    def calculate_price(self, base_price):
        if self._coupon:
            return self._coupon.apply(base_price)
        return base_price

    def _transition(self, action):
        if action not in ALLOWED_TRANSITIONS[self._status]:
            raise InvalidStateTransitionError()
        self._status = ALLOWED_TRANSITIONS[self._status][action]

    def mark_as_paid(self, amount):
        self._paid_amount = amount
        self._transition(OrderAction.PAY)
        self._events.append(OrderPaid(self._id, amount))


# アプリケーション層

class ReceiptSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EventHandler(ABC):
    @abstractmethod
    def handle(self, event: DomainEvent):
        pass


class PayOrderUseCase:
    def __init__(self, order_repo, user_repo, product_repo, dispatcher):
        self._order_repo = order_repo
        self._user_repo = user_repo
        self._product_repo = product_repo
        self._dispatcher = dispatcher

    def execute(self, order_id):
        #データ取得
        order = self._order_repo.get(order_id)
        user = self._user_repo.get(order.user_id)
        product = self._product_repo.get(order.product_id)

        #ビジネス処理
        price = order.calculate_price(product.price)

        user.pay(price)
        product.decrease_stock()
        order.mark_as_paid(price)

        #永続化
        self._user_repo.save(user)
        self._product_repo.save(product)
        self._order_repo.save(order)

        #イベント処理
        self._dispatcher.dispatch(order.events)
        order.clear_events()


# インフラ層

class EventDispatcher:
    def __init__(self):
        self._handlers = {}

    def register(self, event_type, handler):
        self._handlers.setdefault(event_type, []).append(handler)

    def dispatch(self, events):
        for event in events:
            for event_type, handlers in self._handlers.items():
                if isinstance(event, event_type):
                    for handler in handlers:
                        handler.handle(event)


class OrderPaidHandler(EventHandler):
    def __init__(self, sender: ReceiptSender):
        self._sender = sender

    def handle(self, event: OrderPaid):
        self._sender.send(f"Payment completed: {event.amount}")


class EmailReceiptSender(ReceiptSender):
    def send(self, message: str):
        print("[EMAIL]", message)


#InMemory Repository
class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._data = {}

    def get(self, order_id):
        return self._data[order_id.value]

    def save(self, order):
        self._data[order.id.value] = order


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._data = {}

    def get(self, user_id):
        return self._data[user_id]

    def save(self, user):
        self._data[user.id] = user


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self._data = {}

    def get(self, product_id):
        return self._data[product_id]

    def save(self, product):
        self._data[product.id] = product
