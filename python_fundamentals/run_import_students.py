#ファイル分割 ＋ import
#students.py内の関数を別ファイルで使用する時の方法
from students import get_passed_names

scores = {
    "Alice": 80,
    "Bob": 90,
    "Charlie": 55,
    "David": 40
}

passed = get_passed_names(scores)

if passed:
    print("合格者:", passed)
else:
    print("合格者なし")

from students import find_top_student

top_student = find_top_student(scores)

if top_student:
    print("最高得点者:", top_student)
else:
    print("該当なし")