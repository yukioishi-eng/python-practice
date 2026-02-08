#if __name__ == "__main__"の使い方
import students
print("main running")
#students.pyのif __name__ == "__main__"は直接実行されないと条件を満たさない
#今回はmain.pyからの実行なので、print("students loaded")は実行されない