#Optional を用いた関数
from typing import Optional
def first_over_threshold(numbers: list[int], threshold: int) -> Optional[int]:
    """
    return first number which more bigger than threshold
    """
    for n in numbers:
        if n >= threshold:
            return n
    return None

print(first_over_threshold([10, 20, 30], 25))  # 30
print(first_over_threshold([1, 2, 3], 10))    # None