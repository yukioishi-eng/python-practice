# Python Learning & Design Practice

## 概要 (Overview)

Pythonの基礎からオブジェクト指向設計までを学習するためのリポジトリです。

This repository documents my progression from Python fundamentals to small-scale design-oriented implementations.

---

## Contents

### 1. 基本文法の学習
- 変数・データ型
- if / for
- list / dict
- 関数
- 例外処理

### 2. 小規模プログラム
- 成績管理プログラム
- その他の演習コード

### 3. 設計を意識した実装：Order System
- Product / User / Coupon / Order のドメイン設計
- CheckoutService による責務分離
- Enumによる注文状態管理（CREATED / PAID / CANCELED）
- 不正な状態遷移の防止
- 支払い金額を保持した安全なキャンセル処理

---

## 設計で意識したこと

- クラスごとの責務の明確化
- 状態管理の安全性
- ドメインオブジェクトによる整合性維持
- 副作用の順序を考慮した実装

---

## 技術スタック

- Python
- Enum
- Git / GitHub

---

## 今後の改善

- pytestによるユニットテスト追加
- 型ヒントの強化
- API化（FastAPI）
