"""
学習ログ

2026-01-31
内容：
・if文とfor文の復習
・リストから条件に合う要素を取り出す練習
"""

scores = [78, 92, 85, 60, 88]

passed = []

for s in scores:
    if s >= 80:
        passed.append(s)

print("80点以上:", passed)
