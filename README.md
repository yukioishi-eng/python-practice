# Python Practice & Portfolio

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square&logo=fastapi)
![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC?style=flat-square&logo=pytest)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Pythonの基礎文法からドメイン駆動設計（DDD）、FastAPIによるWeb API構築、データ分析までを段階的に学習・実践するためのリポジトリです。

---

## 📌 概要 (Overview)

本リポジトリは、Pythonにおける堅牢なアーキテクチャ設計やAPI開発、データ処理の実践コードを体系的にまとめています。

- **Domain-Driven Design (DDD)**: 注文管理システム（`order_system/`）を題材にした値オブジェクト、エンティティ、ビジネスルールの保護の実践
- **Web API Development**: FastAPIを用いたRESTful APIの構築と Pydantic によるスキーマ定義（`fastapi_practice/`）
- **Data Analysis**: NumPy / Pandas を用いたデータ加工・集計・可視化（`data_analysis/`）
- **Python Fundamentals**: 基礎文法および各種リファレンス実装（`python_fundamentals/`）

---

## 🛠 技術スタック (Tech Stack)

| カテゴリ | 技術・ツール |
| :--- | :--- |
| **言語** | Python 3.10+ |
| **フレームワーク** | FastAPI, Pydantic, Uvicorn |
| **設計手法** | Domain-Driven Design (DDD), オブジェクト指向設計 |
| **テスト** | pytest |
| **データ分析** | NumPy, Pandas, Matplotlib |
| **開発環境** | VS Code, Cursor, Git / GitHub |

---

## 📂 ディレクトリ構成 (Directory Structure)

```text
python-practice/
├── order_system/             # ドメイン駆動設計（DDD）の実践（注文管理システム）
│   ├── domain.py             # 値オブジェクト・エンティティ定義
│   └── test_order.py         # ドメインルールのテストコード
├── fastapi_practice/         # FastAPIによるWeb API実装演習         
├── python_fundamentals/      # Pythonの基礎文法・基本モジュール
├── data_analysis/            # データ分析・集計スクリプト群
├── main.py                   # メインエントリーポイント
├── python_reference.py       # リファレンス・検証用コード
├── requirements.txt          # 依存ライブラリ一覧
└── README.md                 # 本ドキュメント