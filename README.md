# Python Practice — Learning Journal

Pythonの基礎から設計パターンまでを体系的に学習したリポジトリです。
単に「動くコードを書く」だけでなく、**設計の意図・判断の理由**をコメントとログに残しながら進めています。

---

## 学習の流れ

```
基礎文法 → 関数設計 → クラス設計 → 例外設計 → ドメイン設計（DDD）
```

---

## 学習内容

### Phase 1 — 基礎（2026-01）
- `if` 文・`for` 文の復習
- リストからの条件抽出・カウント処理

### Phase 2 — 関数設計（2026-02 前半）
- `None` / `Optional` の使い分けと設計判断
- `raise ValueError` との使い分け
- 型ヒント・docstring による可読性向上
- ファイル分割・`import` の実践
- `if __name__ == "__main__"` の活用

### Phase 3 — クラス設計（2026-02 中盤）
- コンストラクタでのバリデーション
- `@property` / getter / setter によるカプセル化
- mutable（list）と immutable（tuple）の使い分け
- 不変条件（invariant）をクラスで保証する設計

### Phase 4 — 例外・責務分離（2026-02 後半）
- 例外クラスの継承設計
- Service / Domain の責務分離
- 副作用の順序管理と不整合防止
- `pytest` を用いたテスト設計（`pytest.raises` など）

### Phase 5 — ドメイン駆動設計 / DDD（2026-03）
- 状態遷移テーブル（`ALLOWED_TRANSITIONS`）によるテーブル駆動設計
- `Enum` による型安全な状態・操作管理
- ドメインイベントの設計と副作用の分離
- Aggregate Root（`Order`）による整合性保証
- Repository パターン（抽象クラス + InMemory実装）
- レイヤードアーキテクチャ（Domain → Application → Infrastructure）

---

## 注文システム（メインプロジェクト）

`order_system_v1` ～ `order_system_v5` として段階的に設計を進化させました。

| バージョン | 主な変更 |
|-----------|---------|
| v1〜v2 | 基本的な注文・購入処理の実装 |
| v3 | Service / Domain の責務分離、クーポン割引の独立化 |
| v4 | 状態機械（`OrderStatus` Enum）と状態遷移テーブルの導入 |
| v5 | DDD設計：ドメインイベント・Repository・Aggregate Root の実装 |

---

## ファイル構成（一部）

python-practice/
├── basics/                  # 基礎練習
│   ├── passed_number.py
│   ├── count_number.py
│   ├── calc_passed_avg.py
│   ├── ...
    └── order_system/            # 注文システム（メインプロジェクト）
│       ├── order_system_v3.py
│       ├── order_system_v4.py
│       ├── order_system_v5.py
│       └── test_order_system_v5.py
└── main.py          # 学習ログ（日付・内容・ファイル対応）

---

## 意識したこと

- **設計の判断理由をコメントに残す**（なぜそう書いたかを記録）
- **動くコードより「正しい設計」を優先する
- **コードの変化を v1〜v5 として追跡可能にする

---

## 技術スタック

- Python 3.x
- pytest
- 標準ライブラリのみ（外部依存なし）