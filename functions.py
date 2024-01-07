from random import shuffle


def testing(theory: dict[int, tuple[str, str, str]]) -> int:
	score = 0
	
	tmp = [i for i in range(1, len(theory)+1)]
	shuffle(tmp)
	print("Если захочешь закончить раньше окончания, просто нажми Enter\n")
	
	for i in tmp:
		print(theory[i][0])
		answer = input().strip()
		if answer:
			if answer == theory[i][1]:
				score += 1
				print(f"\nПравильный ответ! +1 балл\nУ тебя уже {score} баллов")
			else:
				print(f"\nНеправильный ответ!\n\n{theory[i][1] + theory[i][2]}\n")
		else:
			print(f"Ты решил закончить. Баллов - {score}")
			break
	return score 
