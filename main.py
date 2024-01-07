from random import shuffle
from theory_1 import triangle


def selecting(rn: list) -> int:
    while True:
        try:
            choice = int(input())
            if choice in rn:
                return choice
            print("Ты ввел неправильную цифру, попробуй еще раз")
        except Exception as e:
            print("Ты ввел что-то не так, попробуй еще раз")

print("Привет, это подготовка нацелена на определение твоего уровня знания теории для ЕГЭ по математике\nЧтобы выбрать из списка, напиши цифру, которая соответствует списку ниже:")
print("1 - Проверка теории по определенному заданию")

choice = selecting([1])

if choice == 1:
    print("Ты выбрал проверку теории по определенному заданию. Чтобы выбрать номер задания, напиши цифру этого задания в ЕГЭ")
    choice = selecting(range(1, 20))
    if choice == 1:
        print("Ты выбрал проверку теории по первому заданию из ЕГЭ по математике. Чтобы выбрать в каком формате провести проверку, напиши цифру, которая соответствует списку ниже:")
        print("1 - случайная")

        choice = selecting([1])

        if choice == 1:
            score = 0
            print("Если захочешь закончить раньше окончания, просто нажми Enter")
            tmp = [i for i in range(1, len(triangle)+1)]
            shuffle(tmp)
            for i in tmp:
                print(triangle[i][0])
                answer = input().strip()
                if answer:
                    if answer == triangle[i][1]:
                        score += 1
                        print(f"\nПравильный ответ! +1 балл\nУ тебя уже {score} баллов")
                    else:
                        print(f"\nНеправильный ответ!\n\n{triangle[i][1] + triangle[i][2]}\n")
                else:
                    print(f"Ты решил закончить. Баллов - {score}")
                    break
            print(f"Ты набрал - {score} баллов")

