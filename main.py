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
#propertyを用いた計算プロパティ（area, full_name）を追加するクラス設計の発展練習
class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def price(self) -> int:
        return self._price
    #返り値を書いた方が良い
    
    @name.setter
    def name(self, value):
        self._validate_name(value)
        self._name = value
    
    @price.setter
    def price(self, value):
        self._validate_price(value)
        self._price = value

    def _validate_name(self, name) -> None:    #値を返さないからNone
        if not isinstance(name, str) or name == "":
            raise ValueError("name is invalid")
    def _validate_price(self, price):
        if not isinstance(price, int) or price < 0:
            raise ValueError("price is invalid")

p = Product("Apple", 120)

print(p.name)   # Apple
print(p.price)  # 120

p.price = 150   # OK

p.price = -10   # ValueError

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    @property
    def width(self) -> int:
        return self._width
    
    @width.setter
    def width(self, value):
        self._validate_width(value)
        self._width = value
    
    @property
    def height(self) -> int:
        return self._height
    
    @height.setter
    def height(self, value):
        self._validate_height(value)
        self._height = value
    
    @property
    def area(self):
        return self._width * self._height
    
    def _validate_width(self, width) -> None:
        if not isinstance(width, int) or width < 1:
            raise ValueError("width is invalid")
    def _validate_height(self, height) -> None:
        if not isinstance(height, int) or height < 1:
            raise ValueError("height is invalid")

r = Rectangle(3, 4)

print(r.area)  # 12

r.width = 5

print(r.area)  # 20

class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._validate_first_name(value)
        self._first_name = value
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._validate_last_name(value)
        self._last_name = value

    @property
    def full_name(self) -> str:
        return f"{self._first_name} {self._last_name}"

    def _validate_first_name(self, name) -> None:
        if not isinstance(name, str) or name == "":
            raise ValueError("first_name is invalid")
    def _validate_last_name(self, name) -> None:
        if not isinstance(name, str) or name == "":
            raise ValueError("last_name is invalid")

user = User("Taro", "Yamada")

print(user.full_name)
# Taro Yamada

user.first_name = "Jiro"

print(user.full_name)
# Jiro Yamada

#「安全な状態管理」と「不変条件の維持」
class BankAccount:
    def __init__(self, owner: str, balance: int):
        if not isinstance(owner, str) or owner =="":
            raise ValueError("owner is invalid")
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("balance is invalid")
        self._owner = owner
        self._balance = balance
    
    @property
    def owner(self) -> str:
        return self._owner
    
    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, amount: int) -> None:
        self._validate_amount(amount)
        self._balance += amount
    
    def withdraw(self, amount: int) -> None:
        self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError("amount is invalid")
        self._balance -= amount

    def _validate_amount(self, amount) -> None:
        if not isinstance(amount, int) or amount <1:
            raise ValueError("amount is invalid")

account = BankAccount("Taro", 1000)

print(account.owner)    # Taro
print(account.balance)  # 1000

account.deposit(500)

print(account.balance)  # 1500

account.withdraw(300)

print(account.balance)  # 1200
"""
account.balance = 999999
"""
    #classの複合処理
class Transaction:
    def __init__(self, type: str, amount: int):
        self._validate_type(type)
        self._validate_amount(amount)
        self._type = type
        self._amount = amount

    
    @property
    def type(self) -> str:
        return self._type
    
    @property
    def amount(self) -> int:
        return self._amount
    
    def _validate_type(self, type) -> None:
        if type != "deposit" and type != "withdraw":
            raise ValueError("type is invalid")
    def _validate_amount(self, amount) -> None:
        if not isinstance(amount, int) or amount < 1:
            raise ValueError("amount is invalid")

class BankAccount:
    def __init__(self, owner: str, balance: int):
        self._transactions = []    #Transactionクラスのインスタンスを格納するリスト
        self._validate_owner(owner)
        self._validate_balance(balance)
        self._owner = owner
        self._balance = balance
    
    @property
    def owner(self) -> str:
        return self._owner
    
    @property
    def balance(self) -> int:
        return self._balance
    
    @property
    def transactions(self) -> tuple[Transaction,...]:
        return tuple(self._transactions)    #タプルに変換して返す

    
    def apply_transaction(self, transaction: Transaction) -> None:
        self._validate_transaction(transaction)
        if transaction.type == "deposit":
            self._balance += transaction.amount
        elif transaction.type == "withdraw":
            if transaction.amount > self._balance:
                raise ValueError("amount is invalid")
            self._balance -= transaction.amount
        self._transactions.append(transaction)    #Transactionクラスのインスタンスをリストに追加
    #transactionは残金の変動を表す

    def _validate_owner(self, owner) -> None:
        if not isinstance(owner, str) or owner == "":
            raise ValueError("owner is invalid")
    def _validate_balance(self, balance) -> None:
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("balance is invalid")
    def _validate_transaction(self, transaction) -> None:
        if not isinstance(transaction, Transaction):
            raise ValueError("transaction is invalid")

account = BankAccount("Taro", 1000)

t1 = Transaction("deposit", 500)
account.apply_transaction(t1)

print(account.balance)  # 1500

t2 = Transaction("withdraw", 300)
account.apply_transaction(t2)

print(account.balance)  # 1200

print(len(account.transactions))  # 2
