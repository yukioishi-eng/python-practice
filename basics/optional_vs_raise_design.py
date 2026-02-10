#Optionalとraiseの設計判断
def max_score(scores: dict[str, int]) -> int:
    """
    Return the maximum score.
    Raise ValueError if scores is empty.
    """
    if not scores:
        raise ValueError("scores is empty.")
    return max(scores.values())
    """
    1. Optional を使うべきケース
    特徴 ）
    ・見つからないのが 想定内
    ・呼び出し側が None を普通に処理できる
    例 ）
    ・検索結果がない
    ・条件に合う人がいない
    ・データはあるけど「該当なし」
    👉 これは異常じゃない

    2.raise を使うべきケース
    特徴 ）
    ・その処理自体が 成立しない
    ・呼び出し側に「それはおかしい」と伝えたい
    例 ）
    ・平均を求めたいのにデータが空
    ・引数の型・値が意味をなさない