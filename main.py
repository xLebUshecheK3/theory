from functions import testing
from theory_1 import Theory


def selecting() -> int:
    try:
        return int(input())
    except Exception:
        return 0

while True:
    print("Введи цифру задания, по которому будет проверка теории:")

    while True:
        match selecting():
            case 1:
                result = testing(Theory.theory1)
                break
            case _:
                print("Ты ввел неправильную цифру, попробуй ещё раз")

    print(f"Ты набрал - {result} баллов!")
